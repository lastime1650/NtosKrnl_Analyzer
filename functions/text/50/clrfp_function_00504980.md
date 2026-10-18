# clrfp

- RVA: `0x00504980`–`0x0050499E` (길이 `30` bytes)
- VA: `0x0000000140504980`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `11`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00504986` → [get_fpsr](get_fpsr_function_00504AB0.md) (function, `0x00504AB0`)
- `0x00504990` → [fclrf](fclrf_function_00504AD0.md) (function, `0x00504AD0`)

### Direct callers
- [raise_exc_ex](raise_exc_ex_function_00504620.md) at `0x005047FF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00504980  40 53                           push rbx
00504982  48 83 EC 20                     sub rsp, 0x20
00504986  E8 25 01 00 00                  call 0x140504ab0
0050498B  8B D8                           mov ebx, eax
0050498D  83 E3 3F                        and ebx, 0x3f
00504990  E8 3B 01 00 00                  call 0x140504ad0
00504995  8B C3                           mov eax, ebx
00504997  48 83 C4 20                     add rsp, 0x20
0050499B  5B                              pop rbx
0050499C  C3                              ret
0050499D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall clrfp(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = get_fpsr(a1, a2, a3, a4);
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) & (63));
    result = fclrf(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
void clrfp(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = get_fpsr(a1, a2, a3, a4);
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) & (63));
    result = fclrf(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00504980&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00504980[BB_00504980]
  bb_0050499D[BB_0050499D]
```
