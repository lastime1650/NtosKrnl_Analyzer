# PopUmpoSendPowerRequestAction

- RVA: `0x007692D4`–`0x00769336` (길이 `98` bytes)
- VA: `0x00000001407692D4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CA9E0`
- 디코드: `27`개 명령, `98/98` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007692F5` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0076931E` → [PopUmpoSendPowerMessage](../../text/23/PopUmpoSendPowerMessage_function_00230730.md) (function, `0x00230730`)

### Direct callers
- [PopPowerRequestNotificationsBegin](../75/PopPowerRequestNotificationsBegin_function_00754B24.md) at `0x00754B7A`
- [PopPowerRequestHandleRequestUpdate](../A6/PopPowerRequestHandleRequestUpdate_function_00A652D8.md) at `0x00A6544E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007692F5` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0076931E` → [PopUmpoSendPowerMessage](../../text/23/PopUmpoSendPowerMessage_function_00230730.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007692D4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007692D9  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
007692DE  57                              push rdi
007692DF  48 83 EC 70                     sub rsp, 0x70
007692E3  8B FA                           mov edi, edx
007692E5  41 8A F0                        mov sil, r8b
007692E8  33 D2                           xor edx, edx
007692EA  8B D9                           mov ebx, ecx
007692EC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007692F1  44 8D 42 48                     lea r8d, [rdx + 0x48]
007692F5  E8 46 D9 F5 FF                  call 0x1406c6c40
007692FA  45 33 C9                        xor r9d, r9d
007692FD  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
00769305  45 33 C0                        xor r8d, r8d
00769308  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
0076930C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00769311  89 7C 24 2C                     mov dword ptr [rsp + 0x2c], edi
00769315  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
0076931A  41 8D 51 48                     lea edx, [r9 + 0x48]
0076931E  E8 0D 74 AC FF                  call 0x140230730
00769323  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00769328  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
0076932C  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
00769330  49 8B E3                        mov rsp, r11
00769333  5F                              pop rdi
00769334  C3                              ret
00769335  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopUmpoSendPowerRequestAction(int a1, int a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (112);
    a2 = 0;
    result = memset(v_stack_m58, a2, a2 + 72, a4);
    a4 = 0;
    v_stack_m58 = 16;
    a3 = 0;
    v_stack_m50 = (unsigned int)((unsigned int)(a1));
    v_stack_m4C = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = 0;
    result = PopUmpoSendPowerMessage(v_stack_m58, a4 + 72, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopUmpoSendPowerRequestAction(int32_t Arg1, int32_t Arg2, uint8_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (112);
    Arg2 = 0;
    result = memset(v_stack_m58, Arg2, Arg2 + 72, Arg4);
    Arg4 = 0;
    v_stack_m58 = 16;
    Arg3 = 0;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg1));
    v_stack_m4C = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = 0;
    result = PopUmpoSendPowerMessage(v_stack_m58, Arg4 + 72, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007692D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007692D4[BB_007692D4]
  bb_00769335[BB_00769335]
```
