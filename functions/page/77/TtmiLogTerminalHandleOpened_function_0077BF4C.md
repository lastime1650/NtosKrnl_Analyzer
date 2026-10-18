# TtmiLogTerminalHandleOpened

- RVA: `0x0077BF4C`–`0x0077C025` (길이 `217` bytes)
- VA: `0x000000014077BF4C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC058`
- 디코드: `51`개 명령, `217/217` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077BF87` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077C00A` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077C016` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmpOpenTerminalHandle](TtmpOpenTerminalHandle_function_0077D490.md) at `0x0077D4CB`

### Static image references
- `0x0077BF5A` → RVA `0x00E0A740` (`.data`; read)
- `0x0077BF68` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077BFE7` → RVA `0x00051EAA` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0077BF87` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077C00A` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077C016` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077BF4C  40 55                           push rbp
0077BF4E  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
0077BF53  48 81 EC C0 00 00 00            sub rsp, 0xc0
0077BF5A  48 8B 05 DF E7 68 00            mov rax, qword ptr [rip + 0x68e7df]
0077BF61  48 33 C4                        xor rax, rsp
0077BF64  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0077BF68  83 3D 59 C9 85 00 05            cmp dword ptr [rip + 0x85c959], 5
0077BF6F  44 8B D2                        mov r10d, edx
0077BF72  44 8B D9                        mov r11d, ecx
0077BF75  0F 86 94 00 00 00               jbe 0x14077c00f
0077BF7B  BA 01 00 00 00                  mov edx, 1
0077BF80  48 8D 0D 41 C9 85 00            lea rcx, [rip + 0x85c941]
0077BF87  E8 14 2B CB FF                  call 0x14042eaa0
0077BF8C  84 C0                           test al, al
0077BF8E  74 7F                           je 0x14077c00f
0077BF90  83 65 13 00                     and dword ptr [rbp + 0x13], 0
0077BF94  48 8D 45 C7                     lea rax, [rbp - 0x39]
0077BF98  83 65 23 00                     and dword ptr [rbp + 0x23], 0
0077BF9C  48 8D 0D 25 C9 85 00            lea rcx, [rip + 0x85c925]
0077BFA3  83 65 33 00                     and dword ptr [rbp + 0x33], 0
0077BFA7  BA 04 00 00 00                  mov edx, 4
0077BFAC  83 65 43 00                     and dword ptr [rbp + 0x43], 0
0077BFB0  48 89 45 07                     mov qword ptr [rbp + 7], rax
0077BFB4  48 8D 45 CB                     lea rax, [rbp - 0x35]
0077BFB8  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0077BFBC  48 8D 45 D7                     lea rax, [rbp - 0x29]
0077BFC0  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0077BFC4  48 8D 45 CF                     lea rax, [rbp - 0x31]
0077BFC8  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0077BFCC  48 8D 45 E7                     lea rax, [rbp - 0x19]
0077BFD0  89 55 0F                        mov dword ptr [rbp + 0xf], edx
0077BFD3  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
0077BFD6  4C 89 45 D7                     mov qword ptr [rbp - 0x29], r8
0077BFDA  45 33 C0                        xor r8d, r8d
0077BFDD  44 89 4D CF                     mov dword ptr [rbp - 0x31], r9d
0077BFE1  45 33 C9                        xor r9d, r9d
0077BFE4  89 55 3F                        mov dword ptr [rbp + 0x3f], edx
0077BFE7  48 8D 15 BC 5E 8D FF            lea rdx, [rip - 0x72a144]
0077BFEE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077BFF3  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
0077BFFB  44 89 5D C7                     mov dword ptr [rbp - 0x39], r11d
0077BFFF  44 89 55 CB                     mov dword ptr [rbp - 0x35], r10d
0077C003  C7 45 2F 08 00 00 00            mov dword ptr [rbp + 0x2f], 8
0077C00A  E8 D1 A0 CA FF                  call 0x1404260e0
0077C00F  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0077C013  48 33 CC                        xor rcx, rsp
0077C016  E8 25 06 F3 FF                  call 0x1406ac640
0077C01B  48 81 C4 C0 00 00 00            add rsp, 0xc0
0077C022  5D                              pop rbp
0077C023  C3                              ret
0077C024  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogTerminalHandleOpened(int a1, int a2, __int64 a3, int a4)
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
    result = (*(unsigned __int64 *)(v_rip + 6875103)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8767833)) <= 5) goto loc_0077C00F;
    result = tlgKeywordOn(v_rip + 8767809, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m98;
        a1 = v_rip + 8767781;
        a2 = 4;
        v_stack_m58 = result;
        result = v_stack_m94;
        v_stack_m48 = result;
        result = v_stack_m88;
        v_stack_m38 = result;
        result = v_stack_m90;
        v_stack_m28 = result;
        result = v_stack_m78;
        v_stack_m50 = a2;
        v_stack_m40 = a2;
        v_stack_m88 = a3;
        a3 = 0;
        v_stack_m90 = a4;
        a4 = 0;
        v_stack_m20 = a2;
        a2 = v_rip - 7512388;
        v_stack_mA0 = result;
        v_stack_mA8 = 6;
        v_stack_m98 = (unsigned int)((unsigned int)(a1));
        v_stack_m94 = (unsigned int)((unsigned int)(a2));
        v_stack_m30 = 8;
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
int64_t TtmiLogTerminalHandleOpened(int32_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
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
    result = (*(uint64_t *)(v_rip + 0x68E7DF)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85C959)) <= 5) goto loc_0077C00F;
    result = tlgKeywordOn(v_rip + 8767809, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m98;
        Arg1 = v_rip + 8767781;
        Arg2 = 4;
        v_stack_m58 = result;
        result = v_stack_m94;
        v_stack_m48 = result;
        result = v_stack_m88;
        v_stack_m38 = result;
        result = v_stack_m90;
        v_stack_m28 = result;
        result = v_stack_m78;
        v_stack_m50 = Arg2;
        v_stack_m40 = Arg2;
        v_stack_m88 = Arg3;
        Arg3 = 0;
        v_stack_m90 = Arg4;
        Arg4 = 0;
        v_stack_m20 = Arg2;
        Arg2 = v_rip - 7512388;
        v_stack_mA0 = result;
        v_stack_mA8 = 6;
        v_stack_m98 = (uint32_t)((uint32_t)(Arg1));
        v_stack_m94 = (uint32_t)((uint32_t)(Arg2));
        v_stack_m30 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (192);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077BF4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077BF4C[BB_0077BF4C]
  bb_0077BF7B[BB_0077BF7B]
  bb_0077BF90[BB_0077BF90]
  bb_0077C00F[BB_0077C00F]
  bb_0077C024[BB_0077C024]
  bb_0077BF4C -->|branch| bb_0077C00F
  bb_0077BF4C -->|fallthrough| bb_0077BF7B
  bb_0077BF7B -->|branch| bb_0077C00F
  bb_0077BF7B -->|fallthrough| bb_0077BF90
  bb_0077BF90 -->|flow| bb_0077C00F
```
