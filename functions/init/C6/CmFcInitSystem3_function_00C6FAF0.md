# CmFcInitSystem3

- RVA: `0x00C6FAF0`–`0x00C6FC7C` (길이 `396` bytes)
- VA: `0x0000000140C6FAF0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073684`
- 디코드: `77`개 명령, `396/396` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00C6FB13` → [TlgRegisterAggregateProvider](../../page/70/TlgRegisterAggregateProvider_function_0070526C.md) (function, `0x0070526C`)
- `0x00C6FB4B` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00C6FC61` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00C6FC6D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmInitSystem2](CmInitSystem2_function_00C6FDD8.md) at `0x00C6FDFD`

### Static image references
- `0x00C6FAFE` → RVA `0x00E0A740` (`.data`; read)
- `0x00C6FB0C` → RVA `0x00E09F20` (`.data`; read)
- `0x00C6FB18` → RVA `0x00FC6B20` (`ALMOSTRO`; read)
- `0x00C6FB5B` → RVA `0x0005607D` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00C6FB13` → [TlgRegisterAggregateProvider](../../page/70/TlgRegisterAggregateProvider_function_0070526C.md) (`INIT` → `PAGE`)
  - `0x00C6FB4B` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`INIT` → `.text`)
  - `0x00C6FC61` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`INIT` → `.text`)
  - `0x00C6FC6D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C6FAF0  40 55                           push rbp
00C6FAF2  48 8D 6C 24 F0                  lea rbp, [rsp - 0x10]
00C6FAF7  48 81 EC 10 01 00 00            sub rsp, 0x110
00C6FAFE  48 8B 05 3B AC 19 00            mov rax, qword ptr [rip + 0x19ac3b]
00C6FB05  48 33 C4                        xor rax, rsp
00C6FB08  48 89 45 00                     mov qword ptr [rbp], rax
00C6FB0C  48 8D 0D 0D A4 19 00            lea rcx, [rip + 0x19a40d]
00C6FB13  E8 54 57 A9 FF                  call 0x14070526c
00C6FB18  48 8B 05 01 70 35 00            mov rax, qword ptr [rip + 0x357001]
00C6FB1F  4C 8B 80 F0 00 00 00            mov r8, qword ptr [rax + 0xf0]
00C6FB26  49 81 C0 40 0E 00 00            add r8, 0xe40
00C6FB2D  83 3D EC A3 19 00 05            cmp dword ptr [rip + 0x19a3ec], 5
00C6FB34  0F 86 2C 01 00 00               jbe 0x140c6fc66
00C6FB3A  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00C6FB44  48 8D 0D D5 A3 19 00            lea rcx, [rip + 0x19a3d5]
00C6FB4B  E8 50 EF 7B FF                  call 0x14042eaa0
00C6FB50  84 C0                           test al, al
00C6FB52  0F 84 0E 01 00 00               je 0x140c6fc66
00C6FB58  41 8A 00                        mov al, byte ptr [r8]
00C6FB5B  48 8D 15 1B 65 3E FF            lea rdx, [rip - 0xc19ae5]
00C6FB62  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00C6FB66  48 8D 0D B3 A3 19 00            lea rcx, [rip + 0x19a3b3]
00C6FB6D  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00C6FB72  48 C7 44 24 78 01 00 00 00      mov qword ptr [rsp + 0x78], 1
00C6FB7B  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00C6FB80  45 33 C9                        xor r9d, r9d
00C6FB83  41 8A 40 01                     mov al, byte ptr [r8 + 1]
00C6FB87  88 44 24 31                     mov byte ptr [rsp + 0x31], al
00C6FB8B  48 8D 44 24 31                  lea rax, [rsp + 0x31]
00C6FB90  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C6FB94  41 8A 40 02                     mov al, byte ptr [r8 + 2]
00C6FB98  88 44 24 32                     mov byte ptr [rsp + 0x32], al
00C6FB9C  48 8D 44 24 32                  lea rax, [rsp + 0x32]
00C6FBA1  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00C6FBA5  41 8B 40 04                     mov eax, dword ptr [r8 + 4]
00C6FBA9  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00C6FBAD  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00C6FBB2  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00C6FBB6  41 8B 40 08                     mov eax, dword ptr [r8 + 8]
00C6FBBA  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00C6FBBE  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00C6FBC3  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00C6FBC7  41 8B 40 0C                     mov eax, dword ptr [r8 + 0xc]
00C6FBCB  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
00C6FBCF  48 8D 44 24 3C                  lea rax, [rsp + 0x3c]
00C6FBD4  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00C6FBD8  41 8B 40 10                     mov eax, dword ptr [r8 + 0x10]
00C6FBDC  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00C6FBE0  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00C6FBE5  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00C6FBE9  41 8B 40 14                     mov eax, dword ptr [r8 + 0x14]
00C6FBED  45 33 C0                        xor r8d, r8d
00C6FBF0  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00C6FBF4  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00C6FBF9  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00C6FBFD  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00C6FC02  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00C6FC06  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00C6FC0B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C6FC10  C7 44 24 20 0B 00 00 00         mov dword ptr [rsp + 0x20], 0xb
00C6FC18  48 C7 45 88 01 00 00 00         mov qword ptr [rbp - 0x78], 1
00C6FC20  48 C7 45 98 01 00 00 00         mov qword ptr [rbp - 0x68], 1
00C6FC28  48 C7 45 A8 04 00 00 00         mov qword ptr [rbp - 0x58], 4
00C6FC30  48 C7 45 B8 04 00 00 00         mov qword ptr [rbp - 0x48], 4
00C6FC38  48 C7 45 C8 04 00 00 00         mov qword ptr [rbp - 0x38], 4
00C6FC40  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
00C6FC48  48 C7 45 E8 04 00 00 00         mov qword ptr [rbp - 0x18], 4
00C6FC50  48 C7 44 24 48 00 00 00 01      mov qword ptr [rsp + 0x48], 0x1000000
00C6FC59  48 C7 45 F8 08 00 00 00         mov qword ptr [rbp - 8], 8
00C6FC61  E8 7A 64 7B FF                  call 0x1404260e0
00C6FC66  48 8B 4D 00                     mov rcx, qword ptr [rbp]
00C6FC6A  48 33 CC                        xor rcx, rsp
00C6FC6D  E8 CE C9 A3 FF                  call 0x1406ac640
00C6FC72  48 81 C4 10 01 00 00            add rsp, 0x110
00C6FC79  5D                              pop rbp
00C6FC7A  C3                              ret
00C6FC7B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmFcInitSystem3(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int8 v_stack_mE6;
    unsigned __int8 v_stack_mE7;
    unsigned __int8 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;

    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 1682491)) ^ (v_rsp);
    v_stack_m18 = result;
    result = TlgRegisterAggregateProvider(v_rip + 1680397, a2, a3, a4);
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3502081) + 240)) + (0xE40ULL);
    if ((*(unsigned int *)(v_rip + 1680364)) <= 5) goto loc_00C6FC66;
    result = tlgKeywordOn(v_rip + 1680341, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int8 *)(a3);
        a2 = v_rip - 12688101;
        v_stack_mE8 = (unsigned __int8)(result);
        a1 = v_rip + 1680307;
        result = v_stack_mE8;
        v_stack_mA0 = 1;
        v_stack_mA8 = result;
        a4 = 0;
        result = *(unsigned __int8 *)(a3 + 1);
        v_stack_mE7 = (unsigned __int8)(result);
        result = v_stack_mE7;
        v_stack_m98 = result;
        result = *(unsigned __int8 *)(a3 + 2);
        v_stack_mE6 = (unsigned __int8)(result);
        result = v_stack_mE6;
        v_stack_m88 = result;
        result = *(unsigned int *)(a3 + 4);
        v_stack_mE4 = (unsigned int)(result);
        result = v_stack_mE4;
        v_stack_m78 = result;
        result = *(unsigned int *)(a3 + 8);
        v_stack_mE0 = (unsigned int)(result);
        result = v_stack_mE0;
        v_stack_m68 = result;
        result = *(unsigned int *)(a3 + 12);
        v_stack_mDC = (unsigned int)(result);
        result = v_stack_mDC;
        v_stack_m58 = result;
        result = *(unsigned int *)(a3 + 16);
        v_stack_mD8 = (unsigned int)(result);
        result = v_stack_mD8;
        v_stack_m48 = result;
        result = *(unsigned int *)(a3 + 20);
        a3 = 0;
        v_stack_mD4 = (unsigned int)(result);
        result = v_stack_mD4;
        v_stack_m38 = result;
        result = v_stack_mD0;
        v_stack_m28 = result;
        result = v_stack_mC8;
        v_stack_mF0 = result;
        v_stack_mF8 = 11;
        v_stack_m90 = 1;
        v_stack_m80 = 1;
        v_stack_m70 = 4;
        v_stack_m60 = 4;
        v_stack_m50 = 4;
        v_stack_m40 = 4;
        v_stack_m30 = 4;
        v_stack_mD0 = 0x1000000ULL;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (272);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmFcInitSystem3(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint8_t v_stack_mE6;
    uint8_t v_stack_mE7;
    uint8_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;

    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x19AC3B)) ^ (local_rsp);
    v_stack_m18 = result;
    result = TlgRegisterAggregateProvider(v_rip + 1680397, Arg2, Arg3, Arg4);
    Arg3 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x357001) + 0xF0)) + (0xE40ULL);
    if ((*(uint32_t *)(v_rip + 0x19A3EC)) <= 5) goto loc_00C6FC66;
    result = tlgKeywordOn(v_rip + 1680341, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = *(uint8_t *)(Arg3);
        Arg2 = v_rip - 12688101;
        v_stack_mE8 = (uint8_t)(result);
        Arg1 = v_rip + 1680307;
        result = v_stack_mE8;
        v_stack_mA0 = 1;
        v_stack_mA8 = result;
        Arg4 = 0;
        result = *(uint8_t *)(Arg3 + 0x1);
        v_stack_mE7 = (uint8_t)(result);
        result = v_stack_mE7;
        v_stack_m98 = result;
        result = *(uint8_t *)(Arg3 + 0x2);
        v_stack_mE6 = (uint8_t)(result);
        result = v_stack_mE6;
        v_stack_m88 = result;
        result = *(uint32_t *)(Arg3 + 0x4);
        v_stack_mE4 = (uint32_t)(result);
        result = v_stack_mE4;
        v_stack_m78 = result;
        result = *(uint32_t *)(Arg3 + 0x8);
        v_stack_mE0 = (uint32_t)(result);
        result = v_stack_mE0;
        v_stack_m68 = result;
        result = *(uint32_t *)(Arg3 + 0xC);
        v_stack_mDC = (uint32_t)(result);
        result = v_stack_mDC;
        v_stack_m58 = result;
        result = *(uint32_t *)(Arg3 + 0x10);
        v_stack_mD8 = (uint32_t)(result);
        result = v_stack_mD8;
        v_stack_m48 = result;
        result = *(uint32_t *)(Arg3 + 0x14);
        Arg3 = 0;
        v_stack_mD4 = (uint32_t)(result);
        result = v_stack_mD4;
        v_stack_m38 = result;
        result = v_stack_mD0;
        v_stack_m28 = result;
        result = v_stack_mC8;
        v_stack_mF0 = result;
        v_stack_mF8 = 11;
        v_stack_m90 = 1;
        v_stack_m80 = 1;
        v_stack_m70 = 4;
        v_stack_m60 = 4;
        v_stack_m50 = 4;
        v_stack_m40 = 4;
        v_stack_m30 = 4;
        v_stack_mD0 = 0x1000000ULL;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (272);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C6FAF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C6FAF0[BB_00C6FAF0]
  bb_00C6FB3A[BB_00C6FB3A]
  bb_00C6FB58[BB_00C6FB58]
  bb_00C6FC66[BB_00C6FC66]
  bb_00C6FC7B[BB_00C6FC7B]
  bb_00C6FAF0 -->|branch| bb_00C6FC66
  bb_00C6FAF0 -->|fallthrough| bb_00C6FB3A
  bb_00C6FB3A -->|branch| bb_00C6FC66
  bb_00C6FB3A -->|fallthrough| bb_00C6FB58
  bb_00C6FB58 -->|flow| bb_00C6FC66
```
