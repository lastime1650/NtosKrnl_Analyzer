# PopDirectedDripsDiagTraceDfxPowerStateFailure

- RVA: `0x005DD2B4`–`0x005DD3A3` (길이 `239` bytes)
- VA: `0x00000001405DD2B4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C6160`
- 디코드: `55`개 명령, `239/239` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x005DD2EF` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005DD388` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005DD394` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopFxEnforceDirectedPowerTransition](PopFxEnforceDirectedPowerTransition_function_005D2ACC.md) at `0x005D2AE8`

### Static image references
- `0x005DD2C6` → RVA `0x00E0A740` (`.data`; read)
- `0x005DD2D4` → RVA `0x00E67858` (`.data`; read)
- `0x005DD2E1` → RVA `0x00F0B408` (`.data`; read)
- `0x005DD2E8` → RVA `0x00021F90` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DD2B4  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
005DD2B9  55                              push rbp
005DD2BA  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
005DD2BF  48 81 EC A0 00 00 00            sub rsp, 0xa0
005DD2C6  48 8B 05 73 D4 82 00            mov rax, qword ptr [rip + 0x82d473]
005DD2CD  48 33 C4                        xor rax, rsp
005DD2D0  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
005DD2D4  80 3D 7D A5 88 00 00            cmp byte ptr [rip + 0x88a57d], 0
005DD2DB  0F 84 AC 00 00 00               je 0x1405dd38d
005DD2E1  48 8B 0D 20 E1 92 00            mov rcx, qword ptr [rip + 0x92e120]
005DD2E8  48 8D 15 A1 4C A4 FF            lea rdx, [rip - 0x5bb35f]
005DD2EF  E8 5C 51 DB FF                  call 0x140392450
005DD2F4  84 C0                           test al, al
005DD2F6  0F 84 91 00 00 00               je 0x1405dd38d
005DD2FC  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
005DD300  48 8D 15 89 4C A4 FF            lea rdx, [rip - 0x5bb377]
005DD307  48 83 C1 30                     add rcx, 0x30
005DD30B  41 B9 04 00 00 00               mov r9d, 4
005DD311  4C 8B 01                        mov r8, qword ptr [rcx]
005DD314  41 0F B7 40 28                  movzx eax, word ptr [r8 + 0x28]
005DD319  83 65 13 00                     and dword ptr [rbp + 0x13], 0
005DD31D  83 65 23 00                     and dword ptr [rbp + 0x23], 0
005DD321  83 65 33 00                     and dword ptr [rbp + 0x33], 0
005DD325  D1 E8                           shr eax, 1
005DD327  89 45 F7                        mov dword ptr [rbp - 9], eax
005DD32A  48 8D 45 67                     lea rax, [rbp + 0x67]
005DD32E  48 89 45 07                     mov qword ptr [rbp + 7], rax
005DD332  B8 08 00 00 00                  mov eax, 8
005DD337  89 45 0F                        mov dword ptr [rbp + 0xf], eax
005DD33A  89 45 1F                        mov dword ptr [rbp + 0x1f], eax
005DD33D  48 8D 45 F7                     lea rax, [rbp - 9]
005DD341  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
005DD345  48 89 4D 17                     mov qword ptr [rbp + 0x17], rcx
005DD349  44 89 4D 2F                     mov dword ptr [rbp + 0x2f], r9d
005DD34D  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
005DD351  41 0F B7 48 28                  movzx ecx, word ptr [r8 + 0x28]
005DD356  45 33 C0                        xor r8d, r8d
005DD359  83 65 43 00                     and dword ptr [rbp + 0x43], 0
005DD35D  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
005DD361  48 8D 45 07                     lea rax, [rbp + 7]
005DD365  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005DD36A  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
005DD36F  45 33 C9                        xor r9d, r9d
005DD372  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005DD378  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005DD37E  89 4D 3F                        mov dword ptr [rbp + 0x3f], ecx
005DD381  48 8B 0D 80 E0 92 00            mov rcx, qword ptr [rip + 0x92e080]
005DD388  E8 43 1D C8 FF                  call 0x14025f0d0
005DD38D  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
005DD391  48 33 CC                        xor rcx, rsp
005DD394  E8 A7 F2 0C 00                  call 0x1406ac640
005DD399  48 81 C4 A0 00 00 00            add rsp, 0xa0
005DD3A0  5D                              pop rbp
005DD3A1  C3                              ret
005DD3A2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDirectedDripsDiagTraceDfxPowerStateFailure(__int64 a1)
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
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 8574067)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 8955261)) == 0) goto loc_005DD38D;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9625888), v_rip - 6009695, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = v_stack_p8;
        a2 = v_rip - 6009719;
        a1 = (a1) + (48);
        a4 = 4;
        a3 = *(unsigned __int64 *)(a1);
        result = *(unsigned __int16 *)(a3 + 40);
        result = (unsigned int)((result) >> (1));
        v_stack_m68 = (unsigned int)(result);
        result = v_stack_p8;
        v_stack_m58 = result;
        result = 8;
        v_stack_m50 = (unsigned int)(result);
        v_stack_m40 = (unsigned int)(result);
        result = v_stack_m68;
        v_stack_m38 = result;
        v_stack_m48 = a1;
        v_stack_m30 = (unsigned int)(a4);
        result = *(unsigned __int64 *)(a3 + 48);
        a1 = *(unsigned __int16 *)(a3 + 40);
        a3 = 0;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m70 = result;
        v_stack_m78 = (unsigned int)(a4);
        a4 = 0;
        v_stack_m20 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9625728);
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDirectedDripsDiagTraceDfxPowerStateFailure(int64_t Arg1)
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
    uint64_t v_stack_m5F;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x82D473)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x88A57D)) == 0) goto loc_005DD38D;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x92E120), v_rip - 6009695, a3, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = v_stack_p8;
        a2 = v_rip - 6009719;
        Arg1 = (Arg1) + (48);
        a4 = 4;
        a3 = *(uint64_t *)(Arg1);
        result = *(uint16_t *)(a3 + 0x28);
        result = (uint32_t)((result) >> (1));
        v_stack_m68 = (uint32_t)(result);
        result = v_stack_p8;
        v_stack_m58 = result;
        result = 8;
        v_stack_m50 = (uint32_t)(result);
        v_stack_m40 = (uint32_t)(result);
        result = v_stack_m68;
        v_stack_m38 = result;
        v_stack_m48 = Arg1;
        v_stack_m30 = (uint32_t)(a4);
        result = *(uint64_t *)(a3 + 0x30);
        Arg1 = *(uint16_t *)(a3 + 0x28);
        a3 = 0;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m70 = result;
        v_stack_m78 = (uint32_t)(a4);
        a4 = 0;
        v_stack_m20 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x92E080);
        result = EtwWriteEx(Arg1, a2, a3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DD2B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005DD2B4[BB_005DD2B4]
  bb_005DD2E1[BB_005DD2E1]
  bb_005DD2FC[BB_005DD2FC]
  bb_005DD38D[BB_005DD38D]
  bb_005DD3A2[BB_005DD3A2]
  bb_005DD2B4 -->|branch| bb_005DD38D
  bb_005DD2B4 -->|fallthrough| bb_005DD2E1
  bb_005DD2E1 -->|branch| bb_005DD38D
  bb_005DD2E1 -->|fallthrough| bb_005DD2FC
  bb_005DD2FC -->|flow| bb_005DD38D
```
