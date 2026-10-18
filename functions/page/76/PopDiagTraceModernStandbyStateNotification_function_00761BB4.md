# PopDiagTraceModernStandbyStateNotification

- RVA: `0x00761BB4`–`0x00761CA3` (길이 `239` bytes)
- VA: `0x0000000140761BB4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A6C08`
- 디코드: `57`개 명령, `239/239` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00761BFA` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00761C88` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00761C94` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopModernStandbyNotificationCallback](PopModernStandbyNotificationCallback_function_0076AE00.md) at `0x0076AF98`

### Static image references
- `0x00761BD1` → RVA `0x00E0A740` (`.data`; read)
- `0x00761BDF` → RVA `0x00E67858` (`.data`; read)
- `0x00761BEC` → RVA `0x00F0B408` (`.data`; read)
- `0x00761BF3` → RVA `0x00023388` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00761BFA` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00761C88` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00761C94` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00761BB4  48 8B C4                        mov rax, rsp
00761BB7  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00761BBB  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00761BBF  89 50 10                        mov dword ptr [rax + 0x10], edx
00761BC2  89 48 08                        mov dword ptr [rax + 8], ecx
00761BC5  55                              push rbp
00761BC6  48 8D 68 B1                     lea rbp, [rax - 0x4f]
00761BCA  48 81 EC A0 00 00 00            sub rsp, 0xa0
00761BD1  48 8B 05 68 8B 6A 00            mov rax, qword ptr [rip + 0x6a8b68]
00761BD8  48 33 C4                        xor rax, rsp
00761BDB  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00761BDF  80 3D 72 5C 70 00 00            cmp byte ptr [rip + 0x705c72], 0
00761BE6  0F 84 A1 00 00 00               je 0x140761c8d
00761BEC  48 8B 0D 15 98 7A 00            mov rcx, qword ptr [rip + 0x7a9815]
00761BF3  48 8D 15 8E 17 8C FF            lea rdx, [rip - 0x73e872]
00761BFA  E8 51 08 C3 FF                  call 0x140392450
00761BFF  84 C0                           test al, al
00761C01  0F 84 86 00 00 00               je 0x140761c8d
00761C07  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
00761C0B  48 8D 45 57                     lea rax, [rbp + 0x57]
00761C0F  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
00761C13  48 8D 15 6E 17 8C FF            lea rdx, [rip - 0x73e892]
00761C1A  83 65 03 00                     and dword ptr [rbp + 3], 0
00761C1E  B9 04 00 00 00                  mov ecx, 4
00761C23  83 65 13 00                     and dword ptr [rbp + 0x13], 0
00761C27  45 33 C0                        xor r8d, r8d
00761C2A  83 65 23 00                     and dword ptr [rbp + 0x23], 0
00761C2E  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00761C32  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00761C36  44 8D 49 02                     lea r9d, [rcx + 2]
00761C3A  48 8D 45 5F                     lea rax, [rbp + 0x5f]
00761C3E  89 4D DF                        mov dword ptr [rbp - 0x21], ecx
00761C41  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00761C45  48 8D 45 67                     lea rax, [rbp + 0x67]
00761C49  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00761C4D  48 8D 45 6F                     lea rax, [rbp + 0x6f]
00761C51  48 89 45 07                     mov qword ptr [rbp + 7], rax
00761C55  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00761C59  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00761C5D  48 8D 45 7F                     lea rax, [rbp + 0x7f]
00761C61  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00761C65  48 8D 45 D7                     lea rax, [rbp - 0x29]
00761C69  89 4D EF                        mov dword ptr [rbp - 0x11], ecx
00761C6C  89 4D FF                        mov dword ptr [rbp - 1], ecx
00761C6F  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
00761C72  89 4D 2F                        mov dword ptr [rbp + 0x2f], ecx
00761C75  48 8B 0D 8C 97 7A 00            mov rcx, qword ptr [rip + 0x7a978c]
00761C7C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00761C81  C7 45 1F 10 00 00 00            mov dword ptr [rbp + 0x1f], 0x10
00761C88  E8 93 AA CB FF                  call 0x14041c720
00761C8D  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
00761C91  48 33 CC                        xor rcx, rsp
00761C94  E8 A7 A9 F4 FF                  call 0x1406ac640
00761C99  48 81 C4 A0 00 00 00            add rsp, 0xa0
00761CA0  5D                              pop rbp
00761CA1  C3                              ret
00761CA2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceModernStandbyStateNotification(int a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m88;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 6982504)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 79 + 55) = result;
    if ((*(unsigned __int8 *)(v_rip + 7363698)) == 0) goto loc_00761C8D;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8034325), v_rip - 7596146, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_rsp - 79 + 87;
        a2 = v_rip - 7596178;
        a1 = 4;
        a3 = 0;
        *(unsigned __int64 *)(v_rsp - 79 - 41) = result;
        a4 = a1 + 2;
        result = v_rsp - 79 + 95;
        *(unsigned int *)(v_rsp - 79 - 33) = a1;
        *(unsigned __int64 *)(v_rsp - 79 - 25) = result;
        result = v_rsp - 79 + 103;
        *(unsigned __int64 *)(v_rsp - 79 - 9) = result;
        result = v_rsp - 79 + 111;
        *(unsigned __int64 *)(v_rsp - 79 + 7) = result;
        result = *(unsigned __int64 *)(v_rsp - 79 + 119);
        *(unsigned __int64 *)(v_rsp - 79 + 23) = result;
        result = v_rsp - 79 + 127;
        *(unsigned __int64 *)(v_rsp - 79 + 39) = result;
        result = v_rsp - 79 - 41;
        *(unsigned int *)(v_rsp - 79 - 17) = a1;
        *(unsigned int *)(v_rsp - 79 - 1) = a1;
        *(unsigned int *)(v_rsp - 79 + 15) = a1;
        *(unsigned int *)(v_rsp - 79 + 47) = a1;
        a1 = *(unsigned __int64 *)(v_rip + 8034188);
        v_stack_m88 = result;
        *(unsigned int *)(v_rsp - 79 + 31) = 16;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 79 + 55)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceModernStandbyStateNotification(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m88;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x6A8B68)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x4F + 0x37) = result;
    if ((*(uint8_t *)(v_rip + 0x705C72)) == 0) goto loc_00761C8D;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7A9815), v_rip - 7596146, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = local_rsp - 79 + 87;
        Arg2 = v_rip - 7596178;
        Arg1 = 4;
        Arg3 = 0;
        *(uint64_t *)(local_rsp - 0x4F - 0x29) = result;
        Arg4 = Arg1 + 2;
        result = local_rsp - 79 + 95;
        *(uint32_t *)(local_rsp - 0x4F - 0x21) = Arg1;
        *(uint64_t *)(local_rsp - 0x4F - 0x19) = result;
        result = local_rsp - 79 + 103;
        *(uint64_t *)(local_rsp - 0x4F - 0x9) = result;
        result = local_rsp - 79 + 111;
        *(uint64_t *)(local_rsp - 0x4F + 0x7) = result;
        result = *(uint64_t *)(local_rsp - 0x4F + 0x77);
        *(uint64_t *)(local_rsp - 0x4F + 0x17) = result;
        result = local_rsp - 79 + 127;
        *(uint64_t *)(local_rsp - 0x4F + 0x27) = result;
        result = local_rsp - 79 - 41;
        *(uint32_t *)(local_rsp - 0x4F - 0x11) = Arg1;
        *(uint32_t *)(local_rsp - 0x4F - 0x1) = Arg1;
        *(uint32_t *)(local_rsp - 0x4F + 0xF) = Arg1;
        *(uint32_t *)(local_rsp - 0x4F + 0x2F) = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0x7A978C);
        v_stack_m88 = result;
        *(uint32_t *)(local_rsp - 0x4F + 0x1F) = 16;
        result = EtwWrite(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x4F + 0x37)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00761BB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00761BB4[BB_00761BB4]
  bb_00761BEC[BB_00761BEC]
  bb_00761C07[BB_00761C07]
  bb_00761C8D[BB_00761C8D]
  bb_00761CA2[BB_00761CA2]
  bb_00761BB4 -->|branch| bb_00761C8D
  bb_00761BB4 -->|fallthrough| bb_00761BEC
  bb_00761BEC -->|branch| bb_00761C8D
  bb_00761BEC -->|fallthrough| bb_00761C07
  bb_00761C07 -->|flow| bb_00761C8D
```
