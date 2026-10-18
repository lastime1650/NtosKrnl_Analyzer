# PopDiagTracePowerRequestChange

- RVA: `0x00477C9C`–`0x00477DAD` (길이 `273` bytes)
- VA: `0x0000000140477C9C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CFB4`
- 디코드: `61`개 명령, `273/273` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00477CD7` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00477D92` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x00477D9E` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopPowerRequestReferenceRelease](PopPowerRequestReferenceRelease_function_004775B0.md) at `0x00477656`
- [PopPowerRequestReferenceAcquire](PopPowerRequestReferenceAcquire_function_004776C0.md) at `0x00477762`

### Static image references
- `0x00477CAE` → RVA `0x00E0A740` (`.data`; read)
- `0x00477CBC` → RVA `0x00E67858` (`.data`; read)
- `0x00477CC9` → RVA `0x00F0B408` (`.data`; read)
- `0x00477CD0` → RVA `0x0001A230` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00477C9C  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00477CA1  55                              push rbp
00477CA2  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00477CA7  48 81 EC C0 00 00 00            sub rsp, 0xc0
00477CAE  48 8B 05 8B 2A 99 00            mov rax, qword ptr [rip + 0x992a8b]
00477CB5  48 33 C4                        xor rax, rsp
00477CB8  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00477CBC  80 3D 95 FB 9E 00 00            cmp byte ptr [rip + 0x9efb95], 0
00477CC3  0F 84 CE 00 00 00               je 0x140477d97
00477CC9  48 8B 0D 38 37 A9 00            mov rcx, qword ptr [rip + 0xa93738]
00477CD0  48 8D 15 59 25 BA FF            lea rdx, [rip - 0x45daa7]
00477CD7  E8 74 A7 F1 FF                  call 0x140392450
00477CDC  84 C0                           test al, al
00477CDE  0F 84 B3 00 00 00               je 0x140477d97
00477CE4  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
00477CE8  48 8D 45 67                     lea rax, [rbp + 0x67]
00477CEC  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
00477CF0  48 8D 15 39 25 BA FF            lea rdx, [rip - 0x45dac7]
00477CF7  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
00477CFB  41 B8 04 00 00 00               mov r8d, 4
00477D01  83 65 03 00                     and dword ptr [rbp + 3], 0
00477D05  45 33 C9                        xor r9d, r9d
00477D08  83 65 13 00                     and dword ptr [rbp + 0x13], 0
00477D0C  83 65 23 00                     and dword ptr [rbp + 0x23], 0
00477D10  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00477D14  83 65 43 00                     and dword ptr [rbp + 0x43], 0
00477D18  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00477D1C  48 8D 41 2C                     lea rax, [rcx + 0x2c]
00477D20  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00477D24  48 8D 41 28                     lea rax, [rcx + 0x28]
00477D28  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00477D2C  48 8D 41 30                     lea rax, [rcx + 0x30]
00477D30  48 89 45 07                     mov qword ptr [rbp + 7], rax
00477D34  48 8D 41 34                     lea rax, [rcx + 0x34]
00477D38  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00477D3C  48 8D 41 38                     lea rax, [rcx + 0x38]
00477D40  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00477D44  48 8D 41 3C                     lea rax, [rcx + 0x3c]
00477D48  48 8B 0D B9 36 A9 00            mov rcx, qword ptr [rip + 0xa936b9]
00477D4F  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00477D53  48 8D 45 D7                     lea rax, [rbp - 0x29]
00477D57  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00477D5C  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00477D64  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00477D6A  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00477D70  44 89 45 EF                     mov dword ptr [rbp - 0x11], r8d
00477D74  44 89 45 FF                     mov dword ptr [rbp - 1], r8d
00477D78  44 89 45 0F                     mov dword ptr [rbp + 0xf], r8d
00477D7C  44 89 45 1F                     mov dword ptr [rbp + 0x1f], r8d
00477D80  44 89 45 2F                     mov dword ptr [rbp + 0x2f], r8d
00477D84  44 89 45 3F                     mov dword ptr [rbp + 0x3f], r8d
00477D88  45 33 C0                        xor r8d, r8d
00477D8B  C7 45 DF 08 00 00 00            mov dword ptr [rbp - 0x21], 8
00477D92  E8 39 73 DE FF                  call 0x14025f0d0
00477D97  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00477D9B  48 33 CC                        xor rcx, rsp
00477D9E  E8 9D 48 23 00                  call 0x1406ac640
00477DA3  48 81 C4 C0 00 00 00            add rsp, 0xc0
00477DAA  5D                              pop rbp
00477DAB  C3                              ret
00477DAC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTracePowerRequestChange(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 10037899)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 10419093)) == 0) goto loc_00477D97;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 11089720), v_rip - 4577959, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = v_stack_p8;
        result = v_stack_p8;
        a2 = v_rip - 4577991;
        a3 = 4;
        a4 = 0;
        v_stack_m88 = result;
        result = a1 + 44;
        v_stack_m78 = result;
        result = a1 + 40;
        v_stack_m68 = result;
        result = a1 + 48;
        v_stack_m58 = result;
        result = a1 + 52;
        v_stack_m48 = result;
        result = a1 + 56;
        v_stack_m38 = result;
        result = a1 + 60;
        a1 = *(unsigned __int64 *)(v_rip + 11089593);
        v_stack_m28 = result;
        result = v_stack_m88;
        v_stack_m90 = result;
        v_stack_m98 = 7;
        v_stack_m70 = (unsigned int)(a3);
        v_stack_m60 = (unsigned int)(a3);
        v_stack_m50 = (unsigned int)(a3);
        v_stack_m40 = (unsigned int)(a3);
        v_stack_m30 = (unsigned int)(a3);
        v_stack_m20 = (unsigned int)(a3);
        a3 = 0;
        v_stack_m80 = 8;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (192);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTracePowerRequestChange(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x992A8B)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x9EFB95)) == 0) goto loc_00477D97;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA93738), v_rip - 4577959, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = v_stack_p8;
        result = v_stack_p8;
        Arg2 = v_rip - 4577991;
        Arg3 = 4;
        Arg4 = 0;
        v_stack_m88 = result;
        result = Arg1 + 44;
        v_stack_m78 = result;
        result = Arg1 + 40;
        v_stack_m68 = result;
        result = Arg1 + 48;
        v_stack_m58 = result;
        result = Arg1 + 52;
        v_stack_m48 = result;
        result = Arg1 + 56;
        v_stack_m38 = result;
        result = Arg1 + 60;
        Arg1 = *(uint64_t *)(v_rip + 0xA936B9);
        v_stack_m28 = result;
        result = v_stack_m88;
        v_stack_m90 = result;
        v_stack_m98 = 7;
        v_stack_m70 = (uint32_t)(Arg3);
        v_stack_m60 = (uint32_t)(Arg3);
        v_stack_m50 = (uint32_t)(Arg3);
        v_stack_m40 = (uint32_t)(Arg3);
        v_stack_m30 = (uint32_t)(Arg3);
        v_stack_m20 = (uint32_t)(Arg3);
        Arg3 = 0;
        v_stack_m80 = 8;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (192);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00477C9C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00477C9C[BB_00477C9C]
  bb_00477CC9[BB_00477CC9]
  bb_00477CE4[BB_00477CE4]
  bb_00477D97[BB_00477D97]
  bb_00477DAC[BB_00477DAC]
  bb_00477C9C -->|branch| bb_00477D97
  bb_00477C9C -->|fallthrough| bb_00477CC9
  bb_00477CC9 -->|branch| bb_00477D97
  bb_00477CC9 -->|fallthrough| bb_00477CE4
  bb_00477CE4 -->|flow| bb_00477D97
```
