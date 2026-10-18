# TtmiLogTerminalHandleClosed

- RVA: `0x0077BE70`–`0x0077BF46` (길이 `214` bytes)
- VA: `0x000000014077BE70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC058`
- 디코드: `52`개 명령, `214/214` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077BEAB` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077BF2B` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077BF37` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmpCloseTerminalHandle](TtmpCloseTerminalHandle_function_0077D390.md) at `0x0077D3F7`

### Static image references
- `0x0077BE7E` → RVA `0x00E0A740` (`.data`; read)
- `0x0077BE8C` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077BF0F` → RVA `0x00052862` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0077BEAB` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077BF2B` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077BF37` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077BE70  40 55                           push rbp
0077BE72  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
0077BE77  48 81 EC C0 00 00 00            sub rsp, 0xc0
0077BE7E  48 8B 05 BB E8 68 00            mov rax, qword ptr [rip + 0x68e8bb]
0077BE85  48 33 C4                        xor rax, rsp
0077BE88  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0077BE8C  83 3D 35 CA 85 00 05            cmp dword ptr [rip + 0x85ca35], 5
0077BE93  44 8B D2                        mov r10d, edx
0077BE96  44 8B D9                        mov r11d, ecx
0077BE99  0F 86 91 00 00 00               jbe 0x14077bf30
0077BE9F  BA 01 00 00 00                  mov edx, 1
0077BEA4  48 8D 0D 1D CA 85 00            lea rcx, [rip + 0x85ca1d]
0077BEAB  E8 F0 2B CB FF                  call 0x14042eaa0
0077BEB0  84 C0                           test al, al
0077BEB2  74 7C                           je 0x14077bf30
0077BEB4  83 65 13 00                     and dword ptr [rbp + 0x13], 0
0077BEB8  8D 4A 03                        lea ecx, [rdx + 3]
0077BEBB  83 65 23 00                     and dword ptr [rbp + 0x23], 0
0077BEBF  8D 51 04                        lea edx, [rcx + 4]
0077BEC2  83 65 33 00                     and dword ptr [rbp + 0x33], 0
0077BEC6  48 8D 45 C7                     lea rax, [rbp - 0x39]
0077BECA  83 65 43 00                     and dword ptr [rbp + 0x43], 0
0077BECE  48 89 45 07                     mov qword ptr [rbp + 7], rax
0077BED2  48 8D 45 CB                     lea rax, [rbp - 0x35]
0077BED6  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0077BEDA  48 8D 45 CF                     lea rax, [rbp - 0x31]
0077BEDE  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0077BEE2  48 8D 45 D7                     lea rax, [rbp - 0x29]
0077BEE6  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0077BEEA  48 8D 45 E7                     lea rax, [rbp - 0x19]
0077BEEE  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
0077BEF1  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
0077BEF4  48 8D 0D CD C9 85 00            lea rcx, [rip + 0x85c9cd]
0077BEFB  4C 89 45 CF                     mov qword ptr [rbp - 0x31], r8
0077BEFF  45 33 C0                        xor r8d, r8d
0077BF02  89 55 2F                        mov dword ptr [rbp + 0x2f], edx
0077BF05  4C 89 4D D7                     mov qword ptr [rbp - 0x29], r9
0077BF09  45 33 C9                        xor r9d, r9d
0077BF0C  89 55 3F                        mov dword ptr [rbp + 0x3f], edx
0077BF0F  48 8D 15 4C 69 8D FF            lea rdx, [rip - 0x7296b4]
0077BF16  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077BF1B  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
0077BF23  44 89 5D C7                     mov dword ptr [rbp - 0x39], r11d
0077BF27  44 89 55 CB                     mov dword ptr [rbp - 0x35], r10d
0077BF2B  E8 B0 A1 CA FF                  call 0x1404260e0
0077BF30  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0077BF34  48 33 CC                        xor rcx, rsp
0077BF37  E8 04 07 F3 FF                  call 0x1406ac640
0077BF3C  48 81 C4 C0 00 00 00            add rsp, 0xc0
0077BF43  5D                              pop rbp
0077BF44  C3                              ret
0077BF45  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogTerminalHandleClosed(int a1, int a2, __int64 a3, __int64 a4)
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
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m94;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;

    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 6875323)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8768053)) <= 5) goto loc_0077BF30;
    result = tlgKeywordOn(v_rip + 8768029, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = 1 + 3;
        a2 = a1 + 4;
        result = v_stack_m98;
        v_stack_m58 = result;
        result = v_stack_m94;
        v_stack_m48 = result;
        result = v_stack_m90;
        v_stack_m38 = result;
        result = v_stack_m88;
        v_stack_m28 = result;
        result = v_stack_m78;
        v_stack_m50 = a1;
        v_stack_m40 = a1;
        a1 = v_rip + 8767949;
        v_stack_m90 = a3;
        a3 = 0;
        v_stack_m30 = a2;
        v_stack_m88 = a4;
        a4 = 0;
        v_stack_m20 = a2;
        a2 = v_rip - 7509684;
        v_stack_mA0 = result;
        v_stack_mA8 = 6;
        v_stack_m98 = (unsigned int)((unsigned int)(a1));
        v_stack_m94 = (unsigned int)((unsigned int)(a2));
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (192);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogTerminalHandleClosed(int32_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
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
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m94;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;

    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x68E8BB)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85CA35)) <= 5) goto loc_0077BF30;
    result = tlgKeywordOn(v_rip + 8768029, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = 1 + 3;
        Arg2 = Arg1 + 4;
        result = v_stack_m98;
        v_stack_m58 = result;
        result = v_stack_m94;
        v_stack_m48 = result;
        result = v_stack_m90;
        v_stack_m38 = result;
        result = v_stack_m88;
        v_stack_m28 = result;
        result = v_stack_m78;
        v_stack_m50 = Arg1;
        v_stack_m40 = Arg1;
        Arg1 = v_rip + 8767949;
        v_stack_m90 = Arg3;
        Arg3 = 0;
        v_stack_m30 = Arg2;
        v_stack_m88 = Arg4;
        Arg4 = 0;
        v_stack_m20 = Arg2;
        Arg2 = v_rip - 7509684;
        v_stack_mA0 = result;
        v_stack_mA8 = 6;
        v_stack_m98 = (uint32_t)((uint32_t)(Arg1));
        v_stack_m94 = (uint32_t)((uint32_t)(Arg2));
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (192);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077BE70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077BE70[BB_0077BE70]
  bb_0077BE9F[BB_0077BE9F]
  bb_0077BEB4[BB_0077BEB4]
  bb_0077BF30[BB_0077BF30]
  bb_0077BF45[BB_0077BF45]
  bb_0077BE70 -->|branch| bb_0077BF30
  bb_0077BE70 -->|fallthrough| bb_0077BE9F
  bb_0077BE9F -->|branch| bb_0077BF30
  bb_0077BE9F -->|fallthrough| bb_0077BEB4
  bb_0077BEB4 -->|flow| bb_0077BF30
```
