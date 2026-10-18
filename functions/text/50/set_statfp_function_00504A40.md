# set_statfp

- RVA: `0x00504A40`–`0x00504A61` (길이 `33` bytes)
- VA: `0x0000000140504A40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `12`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00504A49` → [get_fpsr](get_fpsr_function_00504AB0.md) (function, `0x00504AB0`)
- `0x00504A55` → [set_fpsr](set_fpsr_function_00504AC0.md) (function, `0x00504AC0`)

### Direct callers
- [_exception_enabled](_exception_enabled_function_00503F10.md) at `0x00503F38`
- [_exception_enabled](_exception_enabled_function_00503F10.md) at `0x00503F54`
- [_exception_enabled](_exception_enabled_function_00503F10.md) at `0x00503F70`
- [_exception_enabled](_exception_enabled_function_00503F10.md) at `0x00503F92`
- [_exception_enabled](_exception_enabled_function_00503F10.md) at `0x00503FAC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00504A40  40 53                           push rbx
00504A42  48 83 EC 20                     sub rsp, 0x20
00504A46  48 8B D9                        mov rbx, rcx
00504A49  E8 62 00 00 00                  call 0x140504ab0
00504A4E  83 E3 3F                        and ebx, 0x3f
00504A51  0B C3                           or eax, ebx
00504A53  8B C8                           mov ecx, eax
00504A55  E8 66 00 00 00                  call 0x140504ac0
00504A5A  48 83 C4 20                     add rsp, 0x20
00504A5E  5B                              pop rbx
00504A5F  C3                              ret
00504A60  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall set_statfp(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = get_fpsr(a1, a2, a3, a4);
    v_rbx = (unsigned int)((a1) & (63));
    result = (unsigned int)((result) | ((unsigned int)(v_rbx)));
    result = set_fpsr((unsigned int)((unsigned int)(result)), a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t set_statfp(int64_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = get_fpsr(Arg1, a2, a3, a4);
    local_rbx = (uint32_t)((Arg1) & (63));
    result = (uint32_t)((result) | ((uint32_t)(local_rbx)));
    result = set_fpsr((uint32_t)((uint32_t)(result)), a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00504A40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00504A40[BB_00504A40]
  bb_00504A60[BB_00504A60]
```
