# raise_excf

- RVA: `0x00504940`–`0x0050496B` (길이 `43` bytes)
- VA: `0x0000000140504940`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `10`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00504960` → [raise_exc_ex](raise_exc_ex_function_00504620.md) (function, `0x00504620`)

### Direct callers
- [handle_errorf](handle_errorf_function_00504160.md) at `0x0050424C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00504940  48 83 EC 48                     sub rsp, 0x48
00504944  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00504949  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
00504951  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00504956  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0050495B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00504960  E8 BB FC FF FF                  call 0x140504620
00504965  48 83 C4 48                     add rsp, 0x48
00504969  C3                              ret
0050496A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall raise_excf(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = 1;
    v_stack_m20 = a6;
    v_stack_m28 = a5;
    result = raise_exc_ex(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t raise_excf(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = 1;
    v_stack_m20 = Arg6;
    v_stack_m28 = Arg5;
    result = raise_exc_ex(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00504940&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00504940[BB_00504940]
  bb_0050496A[BB_0050496A]
```
