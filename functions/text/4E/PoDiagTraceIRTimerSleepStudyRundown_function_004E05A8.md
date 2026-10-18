# PoDiagTraceIRTimerSleepStudyRundown

- RVA: `0x004E05A8`–`0x004E0697` (길이 `239` bytes)
- VA: `0x00000001404E05A8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BED68`
- 디코드: `54`개 명령, `239/239` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x004E05F5` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x004E0605` → [RtlInitUnicodeString](../42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x004E0674` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x004E0680` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ExStopRecordingIRTimerExpiries](../../page/AD/ExStopRecordingIRTimerExpiries_function_00AD66A0.md) at `0x00AD66FC`

### Static image references
- `0x004E05C2` → RVA `0x00E0A740` (`.data`; read)
- `0x004E05D0` → RVA `0x00E67858` (`.data`; read)
- `0x004E05E7` → RVA `0x00F0B408` (`.data`; read)
- `0x004E05EE` → RVA `0x00021FE8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004E05A8  48 8B C4                        mov rax, rsp
004E05AB  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
004E05AF  66 89 50 10                     mov word ptr [rax + 0x10], dx
004E05B3  89 48 08                        mov dword ptr [rax + 8], ecx
004E05B6  55                              push rbp
004E05B7  48 8D 68 A1                     lea rbp, [rax - 0x5f]
004E05BB  48 81 EC 90 00 00 00            sub rsp, 0x90
004E05C2  48 8B 05 77 A1 92 00            mov rax, qword ptr [rip + 0x92a177]
004E05C9  48 33 C4                        xor rax, rsp
004E05CC  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
004E05D0  80 3D 81 72 98 00 00            cmp byte ptr [rip + 0x987281], 0
004E05D7  0F 57 C0                        xorps xmm0, xmm0
004E05DA  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
004E05DE  49 8B D8                        mov rbx, r8
004E05E1  0F 84 92 00 00 00               je 0x1404e0679
004E05E7  48 8B 0D 1A AE A2 00            mov rcx, qword ptr [rip + 0xa2ae1a]
004E05EE  48 8D 15 F3 19 B4 FF            lea rdx, [rip - 0x4be60d]
004E05F5  E8 56 1E EB FF                  call 0x140392450
004E05FA  84 C0                           test al, al
004E05FC  74 7B                           je 0x1404e0679
004E05FE  48 8B D3                        mov rdx, rbx
004E0601  48 8D 4D 07                     lea rcx, [rbp + 7]
004E0605  E8 76 A1 F4 FF                  call 0x14042a780
004E060A  83 65 23 00                     and dword ptr [rbp + 0x23], 0
004E060E  48 8D 45 67                     lea rax, [rbp + 0x67]
004E0612  83 65 33 00                     and dword ptr [rbp + 0x33], 0
004E0616  48 8D 15 CB 19 B4 FF            lea rdx, [rip - 0x4be635]
004E061D  83 65 43 00                     and dword ptr [rbp + 0x43], 0
004E0621  45 33 C9                        xor r9d, r9d
004E0624  48 8B 0D DD AD A2 00            mov rcx, qword ptr [rip + 0xa2addd]
004E062B  45 33 C0                        xor r8d, r8d
004E062E  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
004E0632  48 8D 45 6F                     lea rax, [rbp + 0x6f]
004E0636  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
004E063A  48 8B 45 0F                     mov rax, qword ptr [rbp + 0xf]
004E063E  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
004E0642  0F B7 45 07                     movzx eax, word ptr [rbp + 7]
004E0646  89 45 3F                        mov dword ptr [rbp + 0x3f], eax
004E0649  48 8D 45 17                     lea rax, [rbp + 0x17]
004E064D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004E0652  C7 44 24 30 03 00 00 00         mov dword ptr [rsp + 0x30], 3
004E065A  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
004E0660  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
004E0666  C7 45 1F 04 00 00 00            mov dword ptr [rbp + 0x1f], 4
004E066D  C7 45 2F 02 00 00 00            mov dword ptr [rbp + 0x2f], 2
004E0674  E8 57 EA D7 FF                  call 0x14025f0d0
004E0679  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
004E067D  48 33 CC                        xor rcx, rsp
004E0680  E8 BB BF 1C 00                  call 0x1406ac640
004E0685  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
004E068D  48 81 C4 90 00 00 00            add rsp, 0x90
004E0694  5D                              pop rbp
004E0695  C3                              ret
004E0696  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoDiagTraceIRTimerSleepStudyRundown(int a1, unsigned __int16 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    *(unsigned __int16 *)(v_rsp + 16) = a2;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 9609591)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm0;
    if ((*(unsigned __int8 *)(v_rip + 9990785)) == 0) goto loc_004E0679;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10661402), v_rip - 4974093, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a2 = a3;
        a1 = v_rsp - 95 + 7;
        result = RtlInitUnicodeString(a1, a2, a3, a4);
        result = v_rsp - 95 + 103;
        a2 = v_rip - 4974133;
        a4 = 0;
        a1 = *(unsigned __int64 *)(v_rip + 10661341);
        a3 = 0;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        result = v_rsp - 95 + 111;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = *(unsigned __int64 *)(v_rsp - 95 + 15);
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = *(unsigned __int16 *)(v_rsp - 95 + 7);
        *(unsigned int *)(v_rsp - 95 + 63) = (unsigned int)(result);
        result = v_rsp - 95 + 23;
        v_stack_m60 = result;
        v_stack_m68 = 3;
        *(unsigned int *)(v_rsp - 95 + 31) = 4;
        *(unsigned int *)(v_rsp - 95 + 47) = 2;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (144);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PoDiagTraceIRTimerSleepStudyRundown(int32_t Arg1, uint16_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    *(uint16_t *)(local_rsp + 0x10) = Arg2;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x92A177)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm0;
    if ((*(uint8_t *)(v_rip + 0x987281)) == 0) goto loc_004E0679;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA2AE1A), v_rip - 4974093, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg2 = Arg3;
        Arg1 = local_rsp - 95 + 7;
        result = RtlInitUnicodeString(Arg1, Arg2, Arg3, Arg4);
        result = local_rsp - 95 + 103;
        Arg2 = v_rip - 4974133;
        Arg4 = 0;
        Arg1 = *(uint64_t *)(v_rip + 0xA2ADDD);
        Arg3 = 0;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        result = local_rsp - 95 + 111;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = *(uint64_t *)(local_rsp - 0x5F + 0xF);
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = *(uint16_t *)(local_rsp - 0x5F + 0x7);
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = (uint32_t)(result);
        result = local_rsp - 95 + 23;
        v_stack_m60 = result;
        v_stack_m68 = 3;
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = 4;
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = 2;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (144);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004E05A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004E05A8[BB_004E05A8]
  bb_004E05E7[BB_004E05E7]
  bb_004E05FE[BB_004E05FE]
  bb_004E0679[BB_004E0679]
  bb_004E0696[BB_004E0696]
  bb_004E05A8 -->|branch| bb_004E0679
  bb_004E05A8 -->|fallthrough| bb_004E05E7
  bb_004E05E7 -->|branch| bb_004E0679
  bb_004E05E7 -->|fallthrough| bb_004E05FE
  bb_004E05FE -->|flow| bb_004E0679
```
