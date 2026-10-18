# AlpcpWaitForSingleObject

- RVA: `0x0043F680`–`0x0043F708` (길이 `136` bytes)
- VA: `0x000000014043F680`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000898D0`
- 디코드: `35`개 명령, `136/136` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0043F6AA` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0043F6C6` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0043F701` → [AlpcpLogUnwait](../../page/74/AlpcpLogUnwait_function_0074D228.md) (function, `0x0074D228`)

### Direct callers
- [AlpcpReceiveSynchronousReply](../../page/92/AlpcpReceiveSynchronousReply_function_009224F0.md) at `0x0092279D`
- [AlpcpReceiveSynchronousReply](../../page/92/AlpcpReceiveSynchronousReply_function_009224F0.md) at `0x009227D6`

### Static image references
- `0x0043F6DE` → RVA `0x00E66D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0043F701` → [AlpcpLogUnwait](../../page/74/AlpcpLogUnwait_function_0074D228.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043F680  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0043F685  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0043F68A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0043F68F  57                              push rdi
0043F690  48 83 EC 30                     sub rsp, 0x30
0043F694  48 8B E9                        mov rbp, rcx
0043F697  41 0F B6 D9                     movzx ebx, r9b
0043F69B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0043F6A4  41 0F B6 F8                     movzx edi, r8b
0043F6A8  8B F2                           mov esi, edx
0043F6AA  E8 41 F9 E1 FF                  call 0x14025eff0
0043F6AF  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0043F6B4  44 0F B6 CB                     movzx r9d, bl
0043F6B8  44 0F B6 C7                     movzx r8d, dil
0043F6BC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0043F6C1  8B D6                           mov edx, esi
0043F6C3  48 8B CD                        mov rcx, rbp
0043F6C6  E8 E5 EF DC FF                  call 0x14020e6b0
0043F6CB  8B D8                           mov ebx, eax
0043F6CD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0043F6D6  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0043F6DD  90                              nop
0043F6DE  80 3D 1B 76 A2 00 00            cmp byte ptr [rip + 0xa2761b], 0
0043F6E5  75 18                           jne 0x14043f6ff
0043F6E7  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0043F6EC  8B C3                           mov eax, ebx
0043F6EE  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0043F6F3  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0043F6F8  48 83 C4 30                     add rsp, 0x30
0043F6FC  5F                              pop rdi
0043F6FD  C3                              ret
0043F6FE  CC                              int3
0043F6FF  8B CB                           mov ecx, ebx
0043F701  E8 22 DB 30 00                  call 0x14074d228
0043F706  EB DF                           jmp 0x14043f6e7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpWaitForSingleObject(__int64 a1, int a2, unsigned __int8 a3, unsigned __int8 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_stack_m18 = a5;
    result = KeWaitForSingleObject(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 10647067)) != 0) goto loc_0043F6FF;
loc_0043F6E7:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_0043F6FF:
    result = AlpcpLogUnwait((unsigned int)((unsigned int)(v_stack_p8)), (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    goto loc_0043F6E7;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpWaitForSingleObject(int64_t Arg1, int32_t Arg2, uint8_t Arg3, uint8_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    v_stack_m18 = Arg5;
    result = KeWaitForSingleObject(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((*(uint8_t *)(v_rip + 0xA2761B)) != 0) goto loc_0043F6FF;
loc_0043F6E7:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_0043F6FF:
    result = AlpcpLogUnwait((uint32_t)((uint32_t)(v_stack_p8)), (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    goto loc_0043F6E7;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043F680&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043F680[BB_0043F680]
  bb_0043F6E7[BB_0043F6E7]
  bb_0043F6FE[BB_0043F6FE]
  bb_0043F6FF[BB_0043F6FF]
  bb_0043F680 -->|branch| bb_0043F6FF
  bb_0043F680 -->|fallthrough| bb_0043F6E7
  bb_0043F6FE -->|flow| bb_0043F6FF
  bb_0043F6FF -->|branch| bb_0043F6E7
```
