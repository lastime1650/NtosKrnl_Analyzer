# TtmiLogTerminalDisplayTimeouts

- RVA: `0x0077BD64`–`0x0077BE68` (길이 `260` bytes)
- VA: `0x000000014077BD64`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B43CC`
- 디코드: `64`개 명령, `260/260` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077BD9F` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077BE4D` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077BE59` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmiTerminalSetDisplayTimeouts](TtmiTerminalSetDisplayTimeouts_function_0077D204.md) at `0x0077D258`

### Static image references
- `0x0077BD72` → RVA `0x00E0A740` (`.data`; read)
- `0x0077BD80` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077BE3E` → RVA `0x00051A5B` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0077BD9F` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077BE4D` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077BE59` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077BD64  40 55                           push rbp
0077BD66  48 8D 6C 24 B9                  lea rbp, [rsp - 0x47]
0077BD6B  48 81 EC E0 00 00 00            sub rsp, 0xe0
0077BD72  48 8B 05 C7 E9 68 00            mov rax, qword ptr [rip + 0x68e9c7]
0077BD79  48 33 C4                        xor rax, rsp
0077BD7C  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0077BD80  83 3D 41 CB 85 00 05            cmp dword ptr [rip + 0x85cb41], 5
0077BD87  44 8B D2                        mov r10d, edx
0077BD8A  44 8B D9                        mov r11d, ecx
0077BD8D  0F 86 BF 00 00 00               jbe 0x14077be52
0077BD93  BA 01 00 00 00                  mov edx, 1
0077BD98  48 8D 0D 29 CB 85 00            lea rcx, [rip + 0x85cb29]
0077BD9F  E8 FC 2C CB FF                  call 0x14042eaa0
0077BDA4  84 C0                           test al, al
0077BDA6  0F 84 A6 00 00 00               je 0x14077be52
0077BDAC  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
0077BDB0  8D 4A 03                        lea ecx, [rdx + 3]
0077BDB3  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
0077BDB7  8D 51 04                        lea edx, [rcx + 4]
0077BDBA  83 65 03 00                     and dword ptr [rbp + 3], 0
0077BDBE  48 8D 45 97                     lea rax, [rbp - 0x69]
0077BDC2  83 65 13 00                     and dword ptr [rbp + 0x13], 0
0077BDC6  83 65 23 00                     and dword ptr [rbp + 0x23], 0
0077BDCA  83 65 33 00                     and dword ptr [rbp + 0x33], 0
0077BDCE  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
0077BDD2  48 8D 45 9B                     lea rax, [rbp - 0x65]
0077BDD6  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0077BDDA  48 8D 45 9F                     lea rax, [rbp - 0x61]
0077BDDE  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0077BDE2  48 8D 45 A3                     lea rax, [rbp - 0x5d]
0077BDE6  48 89 45 07                     mov qword ptr [rbp + 7], rax
0077BDEA  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0077BDEE  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
0077BDF2  48 8D 45 A7                     lea rax, [rbp - 0x59]
0077BDF6  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0077BDFA  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0077BDFE  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
0077BE02  48 8D 45 AF                     lea rax, [rbp - 0x51]
0077BE06  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0077BE0A  48 8D 45 B7                     lea rax, [rbp - 0x49]
0077BE0E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077BE13  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
0077BE17  89 4D DF                        mov dword ptr [rbp - 0x21], ecx
0077BE1A  89 4D EF                        mov dword ptr [rbp - 0x11], ecx
0077BE1D  44 89 45 9F                     mov dword ptr [rbp - 0x61], r8d
0077BE21  45 33 C0                        xor r8d, r8d
0077BE24  89 4D FF                        mov dword ptr [rbp - 1], ecx
0077BE27  44 89 4D A3                     mov dword ptr [rbp - 0x5d], r9d
0077BE2B  45 33 C9                        xor r9d, r9d
0077BE2E  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
0077BE31  48 8D 0D 90 CA 85 00            lea rcx, [rip + 0x85ca90]
0077BE38  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
0077BE3B  89 55 2F                        mov dword ptr [rbp + 0x2f], edx
0077BE3E  48 8D 15 16 5C 8D FF            lea rdx, [rip - 0x72a3ea]
0077BE45  44 89 5D 97                     mov dword ptr [rbp - 0x69], r11d
0077BE49  44 89 55 9B                     mov dword ptr [rbp - 0x65], r10d
0077BE4D  E8 8E A2 CA FF                  call 0x1404260e0
0077BE52  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
0077BE56  48 33 CC                        xor rcx, rsp
0077BE59  E8 E2 07 F3 FF                  call 0x1406ac640
0077BE5E  48 81 C4 E0 00 00 00            add rsp, 0xe0
0077BE65  5D                              pop rbp
0077BE66  C3                              ret
0077BE67  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogTerminalDisplayTimeouts(int a1, int a2, int a3, int a4, __int64 a5, __int64 a6)
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
    unsigned __int64 v_stack_m4F;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mAC;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB4;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;

    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 6875591)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8768321)) <= 5) goto loc_0077BE52;
    result = tlgKeywordOn(v_rip + 8768297, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = 1 + 3;
        a2 = a1 + 4;
        result = v_stack_mB8;
        v_stack_m78 = result;
        result = v_stack_mB4;
        v_stack_m68 = result;
        result = v_stack_mB0;
        v_stack_m58 = result;
        result = v_stack_mAC;
        v_stack_m48 = result;
        result = a5;
        v_stack_mA8 = result;
        result = v_stack_mA8;
        v_stack_m38 = result;
        result = a6;
        v_stack_mA0 = result;
        result = v_stack_mA0;
        v_stack_m28 = result;
        result = v_stack_m98;
        v_stack_mC0 = result;
        v_stack_mC8 = a2;
        v_stack_m70 = a1;
        v_stack_m60 = a1;
        v_stack_mB0 = a3;
        a3 = 0;
        v_stack_m50 = a1;
        v_stack_mAC = a4;
        a4 = 0;
        v_stack_m40 = a1;
        a1 = v_rip + 8768144;
        v_stack_m30 = a2;
        v_stack_m20 = a2;
        a2 = v_rip - 7513066;
        v_stack_mB8 = (unsigned int)((unsigned int)(a1));
        v_stack_mB4 = (unsigned int)((unsigned int)(a2));
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (224);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogTerminalDisplayTimeouts(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6)
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
    uint64_t v_stack_m4F;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mAC;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB4;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;

    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x68E9C7)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85CB41)) <= 5) goto loc_0077BE52;
    result = tlgKeywordOn(v_rip + 8768297, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = 1 + 3;
        Arg2 = Arg1 + 4;
        result = v_stack_mB8;
        v_stack_m78 = result;
        result = v_stack_mB4;
        v_stack_m68 = result;
        result = v_stack_mB0;
        v_stack_m58 = result;
        result = v_stack_mAC;
        v_stack_m48 = result;
        result = Arg5;
        v_stack_mA8 = result;
        result = v_stack_mA8;
        v_stack_m38 = result;
        result = Arg6;
        v_stack_mA0 = result;
        result = v_stack_mA0;
        v_stack_m28 = result;
        result = v_stack_m98;
        v_stack_mC0 = result;
        v_stack_mC8 = Arg2;
        v_stack_m70 = Arg1;
        v_stack_m60 = Arg1;
        v_stack_mB0 = Arg3;
        Arg3 = 0;
        v_stack_m50 = Arg1;
        v_stack_mAC = Arg4;
        Arg4 = 0;
        v_stack_m40 = Arg1;
        Arg1 = v_rip + 8768144;
        v_stack_m30 = Arg2;
        v_stack_m20 = Arg2;
        Arg2 = v_rip - 7513066;
        v_stack_mB8 = (uint32_t)((uint32_t)(Arg1));
        v_stack_mB4 = (uint32_t)((uint32_t)(Arg2));
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (224);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077BD64&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077BD64[BB_0077BD64]
  bb_0077BD93[BB_0077BD93]
  bb_0077BDAC[BB_0077BDAC]
  bb_0077BE52[BB_0077BE52]
  bb_0077BE67[BB_0077BE67]
  bb_0077BD64 -->|branch| bb_0077BE52
  bb_0077BD64 -->|fallthrough| bb_0077BD93
  bb_0077BD93 -->|branch| bb_0077BE52
  bb_0077BD93 -->|fallthrough| bb_0077BDAC
  bb_0077BDAC -->|flow| bb_0077BE52
```
