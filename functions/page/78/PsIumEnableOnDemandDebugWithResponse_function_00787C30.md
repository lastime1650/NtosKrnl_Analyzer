# PsIumEnableOnDemandDebugWithResponse

- RVA: `0x00787C30`–`0x00787CC0` (길이 `144` bytes)
- VA: `0x0000000140787C30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000718AC`
- 디코드: `36`개 명령, `144/144` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00787C81` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00787C97` → [VslEnableOnDemandDebugWithResponse](../71/VslEnableOnDemandDebugWithResponse_function_00718A48.md) (function, `0x00718A48`)
- `0x00787CA8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE91A4`

### Static image references
- `0x00787C5E` → RVA `0x00FC6A98` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00787CA8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00787C30  4C 8B DC                        mov r11, rsp
00787C33  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00787C37  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
00787C3B  57                              push rdi
00787C3C  48 83 EC 40                     sub rsp, 0x40
00787C40  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00787C49  41 8B F8                        mov edi, r8d
00787C4C  49 83 63 F0 00                  and qword ptr [r11 - 0x10], 0
00787C51  48 8B F2                        mov rsi, rdx
00787C54  49 83 63 E8 00                  and qword ptr [r11 - 0x18], 0
00787C59  BA 00 20 00 00                  mov edx, 0x2000
00787C5E  4C 8B 05 33 EE 83 00            mov r8, qword ptr [rip + 0x83ee33]
00787C65  44 8A 88 32 02 00 00            mov r9b, byte ptr [rax + 0x232]
00787C6C  49 8D 43 20                     lea rax, [r11 + 0x20]
00787C70  49 83 63 20 00                  and qword ptr [r11 + 0x20], 0
00787C75  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00787C79  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00787C81  E8 CA 19 0E 00                  call 0x140869650
00787C86  8B D8                           mov ebx, eax
00787C88  85 C0                           test eax, eax
00787C8A  78 21                           js 0x140787cad
00787C8C  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00787C91  44 8B C7                        mov r8d, edi
00787C94  48 8B D6                        mov rdx, rsi
00787C97  E8 AC 0D F9 FF                  call 0x140718a48
00787C9C  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00787CA1  BA 50 73 51 79                  mov edx, 0x79517350
00787CA6  8B D8                           mov ebx, eax
00787CA8  E8 33 FC B6 FF                  call 0x1402f78e0
00787CAD  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00787CB2  8B C3                           mov eax, ebx
00787CB4  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00787CB9  48 83 C4 40                     add rsp, 0x40
00787CBD  5F                              pop rdi
00787CBE  C3                              ret
00787CBF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsIumEnableOnDemandDebugWithResponse(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 32) = v_rsp + 32;
    v_stack_m28 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(a1, (unsigned int)(0x2000ULL), *(unsigned __int64 *)(v_rip + 8646195), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        a1 = v_stack_p20;
        a3 = (unsigned int)((unsigned int)(a3));
        a2 = a2;
        result = VslEnableOnDemandDebugWithResponse(a1, a2, a3, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        a1 = v_stack_p20;
        a2 = 0x79517350ULL;
        v_rbx = (unsigned int)(result);
        result = ObfDereferenceObjectWithTag(a1, a2, a3, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t PsIumEnableOnDemandDebugWithResponse(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x20) = local_rsp + 32;
    v_stack_m28 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(Arg1, (uint32_t)(0x2000ULL), *(uint64_t *)(v_rip + 0x83EE33), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        Arg1 = v_stack_p20;
        Arg3 = (uint32_t)((uint32_t)(Arg3));
        Arg2 = Arg2;
        result = VslEnableOnDemandDebugWithResponse(Arg1, Arg2, Arg3, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        Arg1 = v_stack_p20;
        Arg2 = 0x79517350ULL;
        local_rbx = (uint32_t)(result);
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, Arg3, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00787C30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00787C30[BB_00787C30]
  bb_00787C8C[BB_00787C8C]
  bb_00787CAD[BB_00787CAD]
  bb_00787CBF[BB_00787CBF]
  bb_00787C30 -->|branch| bb_00787CAD
  bb_00787C30 -->|fallthrough| bb_00787C8C
  bb_00787C8C -->|flow| bb_00787CAD
```
