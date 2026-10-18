# PopTraceSystemIdleS0LowPowerDozeTimerArmed

- RVA: `0x00763EA8`–`0x00763F61` (길이 `185` bytes)
- VA: `0x0000000140763EA8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC790`
- 디코드: `43`개 명령, `185/185` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00763EE6` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00763F09` → [PopDiagInterruptTimeToSystemTime](../../pagelk/B7/PopDiagInterruptTimeToSystemTime_function_00B7D6F4.md) (function, `0x00B7D6F4`)
- `0x00763F41` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00763F4D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopIdleArmAoAcDozeS4Timer](../../text/4E/PopIdleArmAoAcDozeS4Timer_function_004E03A8.md) at `0x004E048C`

### Static image references
- `0x00763EB9` → RVA `0x00E0A740` (`.data`; read)
- `0x00763ECF` → RVA `0x00E67858` (`.data`; read)
- `0x00763ED8` → RVA `0x00F0B408` (`.data`; read)
- `0x00763EDF` → RVA `0x00021C60` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00763EE6` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00763F09` → [PopDiagInterruptTimeToSystemTime](../../pagelk/B7/PopDiagInterruptTimeToSystemTime_function_00B7D6F4.md) (`PAGE` → `PAGELK`)
  - `0x00763F41` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00763F4D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00763EA8  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00763EAD  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00763EB1  55                              push rbp
00763EB2  48 8B EC                        mov rbp, rsp
00763EB5  48 83 EC 60                     sub rsp, 0x60
00763EB9  48 8B 05 80 68 6A 00            mov rax, qword ptr [rip + 0x6a6880]
00763EC0  48 33 C4                        xor rax, rsp
00763EC3  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00763EC7  48 83 65 D0 00                  and qword ptr [rbp - 0x30], 0
00763ECC  48 8B DA                        mov rbx, rdx
00763ECF  80 3D 82 39 70 00 00            cmp byte ptr [rip + 0x703982], 0
00763ED6  74 6E                           je 0x140763f46
00763ED8  48 8B 0D 29 75 7A 00            mov rcx, qword ptr [rip + 0x7a7529]
00763EDF  48 8D 15 7A DD 8B FF            lea rdx, [rip - 0x742286]
00763EE6  E8 65 E5 C2 FF                  call 0x140392450
00763EEB  84 C0                           test al, al
00763EED  74 57                           je 0x140763f46
00763EEF  83 65 E4 00                     and dword ptr [rbp - 0x1c], 0
00763EF3  48 8D 45 10                     lea rax, [rbp + 0x10]
00763EF7  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00763EFB  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00763EFF  48 8B CB                        mov rcx, rbx
00763F02  C7 45 E0 04 00 00 00            mov dword ptr [rbp - 0x20], 4
00763F09  E8 E6 97 41 00                  call 0x140b7d6f4
00763F0E  83 65 F4 00                     and dword ptr [rbp - 0xc], 0
00763F12  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00763F16  48 89 4D E8                     mov qword ptr [rbp - 0x18], rcx
00763F1A  48 8D 45 D8                     lea rax, [rbp - 0x28]
00763F1E  48 8B 0D E3 74 7A 00            mov rcx, qword ptr [rip + 0x7a74e3]
00763F25  48 8D 15 34 DD 8B FF            lea rdx, [rip - 0x7422cc]
00763F2C  41 B9 02 00 00 00               mov r9d, 2
00763F32  C7 45 F0 08 00 00 00            mov dword ptr [rbp - 0x10], 8
00763F39  45 33 C0                        xor r8d, r8d
00763F3C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00763F41  E8 DA 87 CB FF                  call 0x14041c720
00763F46  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00763F4A  48 33 CC                        xor rcx, rsp
00763F4D  E8 EE 86 F4 FF                  call 0x1406ac640
00763F52  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
00763F5A  48 83 C4 60                     add rsp, 0x60
00763F5E  5D                              pop rbp
00763F5F  C3                              ret
00763F60  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopTraceSystemIdleS0LowPowerDozeTimerArmed(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 6973568)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned __int8 *)(v_rip + 7354754)) == 0) goto loc_00763F46;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8025385), v_rip - 7611014, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a2 = v_stack_m38;
        v_stack_m30 = result;
        a1 = a2;
        v_stack_m28 = 4;
        result = PopDiagInterruptTimeToSystemTime(a1, a2, a3, a4);
        a1 = v_stack_m38;
        v_stack_m20 = a1;
        result = v_stack_m30;
        a1 = *(unsigned __int64 *)(v_rip + 8025315);
        a2 = v_rip - 7611084;
        a4 = 2;
        v_stack_m18 = 8;
        a3 = 0;
        v_stack_m48 = result;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopTraceSystemIdleS0LowPowerDozeTimerArmed(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_p18;
    uint32_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x6A6880)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint8_t *)(v_rip + 0x703982)) == 0) goto loc_00763F46;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7A7529), v_rip - 7611014, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg2 = v_stack_m38;
        v_stack_m30 = result;
        Arg1 = Arg2;
        v_stack_m28 = 4;
        result = PopDiagInterruptTimeToSystemTime(Arg1, Arg2, Arg3, a4);
        Arg1 = v_stack_m38;
        v_stack_m20 = Arg1;
        result = v_stack_m30;
        Arg1 = *(uint64_t *)(v_rip + 0x7A74E3);
        Arg2 = v_rip - 7611084;
        a4 = 2;
        v_stack_m18 = 8;
        Arg3 = 0;
        v_stack_m48 = result;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00763EA8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00763EA8[BB_00763EA8]
  bb_00763ED8[BB_00763ED8]
  bb_00763EEF[BB_00763EEF]
  bb_00763F46[BB_00763F46]
  bb_00763F60[BB_00763F60]
  bb_00763EA8 -->|branch| bb_00763F46
  bb_00763EA8 -->|fallthrough| bb_00763ED8
  bb_00763ED8 -->|branch| bb_00763F46
  bb_00763ED8 -->|fallthrough| bb_00763EEF
  bb_00763EEF -->|flow| bb_00763F46
```
