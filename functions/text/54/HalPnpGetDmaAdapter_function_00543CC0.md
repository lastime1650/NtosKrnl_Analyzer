# HalPnpGetDmaAdapter

- RVA: `0x00543CC0`–`0x00543CFD` (길이 `61` bytes)
- VA: `0x0000000140543CC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `18`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00543CDE` → [HalpDmaFindDeviceObjectByToken](../53/HalpDmaFindDeviceObjectByToken_function_0053FD28.md) (function, `0x0053FD28`)
- `0x00543CEC` → [HalpGetAdapter](../../page/70/HalpGetAdapter_function_00706EBC.md) (function, `0x00706EBC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00543CEC` → [HalpGetAdapter](../../page/70/HalpGetAdapter_function_00706EBC.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00543CC0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00543CC5  57                              push rdi
00543CC6  48 83 EC 20                     sub rsp, 0x20
00543CCA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00543CD3  49 8B D8                        mov rbx, r8
00543CD6  48 8B FA                        mov rdi, rdx
00543CD9  45 33 C0                        xor r8d, r8d
00543CDC  33 D2                           xor edx, edx
00543CDE  E8 45 C0 FF FF                  call 0x14053fd28
00543CE3  4C 8B C3                        mov r8, rbx
00543CE6  48 8B D0                        mov rdx, rax
00543CE9  48 8B CF                        mov rcx, rdi
00543CEC  E8 CB 31 1C 00                  call 0x140706ebc
00543CF1  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00543CF6  48 83 C4 20                     add rsp, 0x20
00543CFA  5F                              pop rdi
00543CFB  C3                              ret
00543CFC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalPnpGetDmaAdapter(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = HalpDmaFindDeviceObjectByToken(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    result = HalpGetAdapter(0, result, 0, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalPnpGetDmaAdapter(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = HalpDmaFindDeviceObjectByToken(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, a4);
    result = HalpGetAdapter(0, result, 0, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00543CC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00543CC0[BB_00543CC0]
  bb_00543CFC[BB_00543CFC]
```
