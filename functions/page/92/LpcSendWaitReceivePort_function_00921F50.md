# LpcSendWaitReceivePort

- RVA: `0x00921F50`–`0x00921FC6` (길이 `118` bytes)
- VA: `0x0000000140921F50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008D0E0`
- 디코드: `30`개 명령, `118/118` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00921F95` → [AlpcpProcessSynchronousRequest](AlpcpProcessSynchronousRequest_function_00921FCC.md) (function, `0x00921FCC`)
- `0x00921FB1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [DbgkpSendApiMessageLpc](DbgkpSendApiMessageLpc_function_00920E4C.md) at `0x00920EC6`
- [IopSendMessageToTrackService](../AC/IopSendMessageToTrackService_function_00AC0E5C.md) at `0x00AC107A`
- [sub_00B3E4E0](../B3/Unknown_function_00B3E4E0.md) at `0x00B3E641`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00921FB1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00921F50  4C 8B DC                        mov r11, rsp
00921F53  53                              push rbx
00921F54  48 83 EC 50                     sub rsp, 0x50
00921F58  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00921F61  83 CA 02                        or edx, 2
00921F64  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
00921F69  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00921F70  90                              nop
00921F71  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00921F79  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00921F7D  49 83 63 D8 00                  and qword ptr [r11 - 0x28], 0
00921F82  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00921F8A  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
00921F8E  4D 89 4B C8                     mov qword ptr [r11 - 0x38], r9
00921F92  45 33 C9                        xor r9d, r9d
00921F95  E8 32 00 00 00                  call 0x140921fcc
00921F9A  8B D8                           mov ebx, eax
00921F9C  3D 03 07 00 C0                  cmp eax, 0xc0000703
00921FA1  74 1C                           je 0x140921fbf
00921FA3  81 FB 01 07 00 C0               cmp ebx, 0xc0000701
00921FA9  B8 53 02 00 C0                  mov eax, 0xc0000253
00921FAE  0F 44 D8                        cmove ebx, eax
00921FB1  E8 FA B8 93 FF                  call 0x14025d8b0
00921FB6  8B C3                           mov eax, ebx
00921FB8  48 83 C4 50                     add rsp, 0x50
00921FBC  5B                              pop rbx
00921FBD  C3                              ret
00921FBE  CC                              int3
00921FBF  BB 37 00 00 C0                  mov ebx, 0xc0000037
00921FC4  EB EB                           jmp 0x140921fb1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LpcSendWaitReceivePort(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;

    v_rsp = (v_rsp) - (80);
    a2 = (unsigned int)((a2) | (2));
    v_stack_m18 = 0;
    *(unsigned __int64 *)(v_rsp - 32) = a6;
    *(unsigned __int64 *)(v_rsp - 48) = a5;
    *(unsigned __int64 *)(v_rsp - 56) = a4;
    a4 = 0;
    result = AlpcpProcessSynchronousRequest(a1, a2, a3, a4);
    if (((unsigned int)(result)) == 0xC0000703ULL) goto loc_00921FBF;
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000701ULL) { v_rbx = (unsigned int)((unsigned int)(0xC0000253ULL)); }
loc_00921FB1:
    result = KeLeaveCriticalRegion(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)(v_rbx));
loc_00921FBF:
    goto loc_00921FB1;
}
```

## 5. (Beta) C Style

```c
int64_t LpcSendWaitReceivePort(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint8_t v_stack_m18;

    local_rsp = (local_rsp) - (80);
    Arg2 = (uint32_t)((Arg2) | (2));
    v_stack_m18 = 0;
    *(uint64_t *)(local_rsp - 0x20) = Arg6;
    *(uint64_t *)(local_rsp - 0x30) = Arg5;
    *(uint64_t *)(local_rsp - 0x38) = Arg4;
    Arg4 = 0;
    result = AlpcpProcessSynchronousRequest(Arg1, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) == 0xC0000703ULL) goto loc_00921FBF;
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000701ULL) { local_rbx = (uint32_t)((uint32_t)(0xC0000253ULL)); }
loc_00921FB1:
    result = KeLeaveCriticalRegion(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)(local_rbx));
loc_00921FBF:
    goto loc_00921FB1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00921F50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00921F50[BB_00921F50]
  bb_00921FA3[BB_00921FA3]
  bb_00921FB1[BB_00921FB1]
  bb_00921FBE[BB_00921FBE]
  bb_00921FBF[BB_00921FBF]
  bb_00921F50 -->|branch| bb_00921FBF
  bb_00921F50 -->|fallthrough| bb_00921FA3
  bb_00921FA3 -->|flow| bb_00921FB1
  bb_00921FBE -->|flow| bb_00921FBF
  bb_00921FBF -->|branch| bb_00921FB1
```
