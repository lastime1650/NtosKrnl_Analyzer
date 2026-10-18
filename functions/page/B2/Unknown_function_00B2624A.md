# sub_00B2624A

- RVA: `0x00B2624A`–`0x00B26286` (길이 `60` bytes)
- VA: `0x0000000140B2624A`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00091EA4`
- 디코드: `16`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B2627B` → [McTemplateK0zjqdtd_EtwWriteTransfer](../../text/5A/McTemplateK0zjqdtd_EtwWriteTransfer_function_005A8528.md) (function, `0x005A8528`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B2627B` → [McTemplateK0zjqdtd_EtwWriteTransfer](../../text/5A/McTemplateK0zjqdtd_EtwWriteTransfer_function_005A8528.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B26281` → [PnpInsertEventInQueue + 0x51](../95/PnpInsertEventInQueue_function_00951B78.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B2624A  45 33 C9                        xor r9d, r9d
00B2624D  33 C9                           xor ecx, ecx
00B2624F  48 39 4B 18                     cmp qword ptr [rbx + 0x18], rcx
00B26253  0F 95 C1                        setne cl
00B26256  8B 83 98 00 00 00               mov eax, dword ptr [rbx + 0x98]
00B2625C  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B26260  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
00B26264  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
00B26267  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B2626B  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00B2626E  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00B26272  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B26277  4D 8B 49 30                     mov r9, qword ptr [r9 + 0x30]
00B2627B  E8 A8 22 A8 FF                  call 0x1405a8528
00B26280  90                              nop
00B26281  E9 43 B9 E2 FF                  jmp 0x140951bc9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B2624A(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;

    a4 = 0;
    a1 = 0;
    a1 = ((*(unsigned __int64 *)(v_rbx + 24)) != 0) ? 1 : 0;
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 152)));
    v_stack_p38 = a1;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 20)));
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 16)));
    v_stack_p20 = a2;
    result = McTemplateK0zjqdtd_EtwWriteTransfer(a1, a2, a3, *(unsigned __int64 *)(a4 + 48));
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B2624A(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;

    Arg4 = 0;
    Arg1 = 0;
    Arg1 = ((*(uint64_t *)(local_rbx + 0x18)) != 0) ? 1 : 0;
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x98)));
    v_stack_p38 = Arg1;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x14)));
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x10)));
    v_stack_p20 = Arg2;
    result = McTemplateK0zjqdtd_EtwWriteTransfer(Arg1, Arg2, Arg3, *(uint64_t *)(Arg4 + 0x30));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B2624A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B2624A[BB_00B2624A]
```
