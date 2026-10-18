# CmpLogFlushPhaseEnd

- RVA: `0x00A4D268`–`0x00A4D34E` (길이 `230` bytes)
- VA: `0x0000000140A4D268`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EA9C`
- 디코드: `52`개 명령, `230/230` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00A4D333` → [EtwWriteTransfer](../../text/41/EtwWriteTransfer_function_0041C830.md) (function, `0x0041C830`)
- `0x00A4D33F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) at `0x009B4289`
- [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) at `0x009B42DC`
- [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) at `0x009B4530`
- [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) at `0x009B4570`
- [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) at `0x009B45B1`
- [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) at `0x009B460E`
- [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) at `0x009B468D`

### Static image references
- `0x00A4D276` → RVA `0x00E0A740` (`.data`; read)
- `0x00A4D28A` → RVA `0x00E09F58` (`.data`; read)
- `0x00A4D2B8` → RVA `0x00043590` (`.rdata`; read)
- `0x00A4D2BF` → RVA `0x000561A9` (`.rdata`; read)
- `0x00A4D2C9` → RVA `0x00E09F60` (`.data`; read)
- `0x00A4D2EC` → RVA `0x000561B3` (`.rdata`; read)
- `0x00A4D2F7` → RVA `0x0005BCFD` (`.rdata`; read)
- `0x00A4D31B` → RVA `0x00E09F78` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A4D333` → [EtwWriteTransfer](../../text/41/EtwWriteTransfer_function_0041C830.md) (`PAGE` → `.text`)
  - `0x00A4D33F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4D268  40 55                           push rbp
00A4D26A  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00A4D26F  48 81 EC A0 00 00 00            sub rsp, 0xa0
00A4D276  48 8B 05 C3 D4 3B 00            mov rax, qword ptr [rip + 0x3bd4c3]
00A4D27D  48 33 C4                        xor rax, rsp
00A4D280  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00A4D284  41 B9 04 00 00 00               mov r9d, 4
00A4D28A  44 39 0D C7 CC 3B 00            cmp dword ptr [rip + 0x3bccc7], r9d
00A4D291  0F 86 A1 00 00 00               jbe 0x140a4d338
00A4D297  88 55 E7                        mov byte ptr [rbp - 0x19], dl
00A4D29A  48 8D 45 E7                     lea rax, [rbp - 0x19]
00A4D29E  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00A4D2A2  41 8D 51 FD                     lea edx, [r9 - 3]
00A4D2A6  33 C9                           xor ecx, ecx
00A4D2A8  48 89 55 2F                     mov qword ptr [rbp + 0x2f], rdx
00A4D2AC  48 89 4D FF                     mov qword ptr [rbp - 1], rcx
00A4D2B0  48 8D 45 EB                     lea rax, [rbp - 0x15]
00A4D2B4  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00A4D2B8  48 8D 0D D1 62 5F FF            lea rcx, [rip - 0xa09d2f]
00A4D2BF  0F B7 05 E3 8E 60 FF            movzx eax, word ptr [rip - 0x9f711d]
00A4D2C6  89 45 FB                        mov dword ptr [rbp - 5], eax
00A4D2C9  48 8B 05 90 CC 3B 00            mov rax, qword ptr [rip + 0x3bcc90]
00A4D2D0  48 89 45 07                     mov qword ptr [rbp + 7], rax
00A4D2D4  44 89 45 EB                     mov dword ptr [rbp - 0x15], r8d
00A4D2D8  45 33 C0                        xor r8d, r8d
00A4D2DB  4C 89 4D 3F                     mov qword ptr [rbp + 0x3f], r9
00A4D2DF  C7 45 F7 00 00 00 0B            mov dword ptr [rbp - 9], 0xb000000
00A4D2E6  0F B7 00                        movzx eax, word ptr [rax]
00A4D2E9  89 45 0F                        mov dword ptr [rbp + 0xf], eax
00A4D2EC  48 8D 05 C0 8E 60 FF            lea rax, [rip - 0x9f7140]
00A4D2F3  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00A4D2F7  48 8D 05 FF E9 60 FF            lea rax, [rip - 0x9f1601]
00A4D2FE  2B C1                           sub eax, ecx
00A4D300  89 55 23                        mov dword ptr [rbp + 0x23], edx
00A4D303  C7 45 13 02 00 00 00            mov dword ptr [rbp + 0x13], 2
00A4D30A  48 8D 55 F7                     lea rdx, [rbp - 9]
00A4D30E  C7 45 1F 23 00 00 00            mov dword ptr [rbp + 0x1f], 0x23
00A4D315  89 45 EF                        mov dword ptr [rbp - 0x11], eax
00A4D318  8B 45 EF                        mov eax, dword ptr [rbp - 0x11]
00A4D31B  48 8B 0D 56 CC 3B 00            mov rcx, qword ptr [rip + 0x3bcc56]
00A4D322  48 8D 45 07                     lea rax, [rbp + 7]
00A4D326  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A4D32B  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00A4D330  45 33 C9                        xor r9d, r9d
00A4D333  E8 F8 F4 9C FF                  call 0x14041c830
00A4D338  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00A4D33C  48 33 CC                        xor rcx, rsp
00A4D33F  E8 FC F2 C5 FF                  call 0x1406ac640
00A4D344  48 81 C4 A0 00 00 00            add rsp, 0xa0
00A4D34B  5D                              pop rbp
00A4D34C  C3                              ret
00A4D34D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLogFlushPhaseEnd(int a1, unsigned __int8 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m74;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 3921091)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 3919047)) >= = 4) {
        v_stack_m78 = a2;
        result = v_stack_m78;
        v_stack_m38 = result;
        a2 = 4 - 3;
        a1 = 0;
        v_stack_m30 = a2;
        v_stack_m60 = 0;
        result = v_stack_m74;
        v_stack_m28 = result;
        a1 = v_rip - 10525999;
        result = *(unsigned __int16 *)(v_rip - 10449181);
        v_stack_m64 = (unsigned int)(result);
        result = *(unsigned __int64 *)(v_rip + 3918992);
        v_stack_m58 = result;
        v_stack_m74 = a3;
        a3 = 0;
        v_stack_m20 = 4;
        v_stack_m68 = 0xB000000ULL;
        result = *(unsigned __int16 *)(result);
        v_stack_m50 = (unsigned int)(result);
        result = v_rip - 10449216;
        v_stack_m48 = result;
        result = v_rip - 10425857;
        result = (unsigned int)((result) - (a1));
        v_stack_m3C = a2;
        v_stack_m4C = 2;
        a2 = v_stack_m68;
        v_stack_m40 = 35;
        v_stack_m70 = (unsigned int)(result);
        result = v_stack_m70;
        a1 = *(unsigned __int64 *)(v_rip + 3918934);
        result = v_stack_m58;
        v_stack_m80 = result;
        v_stack_m88 = 4;
        a4 = 0;
        result = EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpLogFlushPhaseEnd(int32_t Arg1, uint8_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m74;
    uint8_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x3BD4C3)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x3BCCC7)) >= = 4) {
        v_stack_m78 = Arg2;
        result = v_stack_m78;
        v_stack_m38 = result;
        Arg2 = 4 - 3;
        Arg1 = 0;
        v_stack_m30 = Arg2;
        v_stack_m60 = 0;
        result = v_stack_m74;
        v_stack_m28 = result;
        Arg1 = v_rip - 10525999;
        result = *(uint16_t *)(v_rip - 0x9F711D);
        v_stack_m64 = (uint32_t)(result);
        result = *(uint64_t *)(v_rip + 0x3BCC90);
        v_stack_m58 = result;
        v_stack_m74 = Arg3;
        Arg3 = 0;
        v_stack_m20 = 4;
        v_stack_m68 = 0xB000000ULL;
        result = *(uint16_t *)(result);
        v_stack_m50 = (uint32_t)(result);
        result = v_rip - 10449216;
        v_stack_m48 = result;
        result = v_rip - 10425857;
        result = (uint32_t)((result) - (Arg1));
        v_stack_m3C = Arg2;
        v_stack_m4C = 2;
        Arg2 = v_stack_m68;
        v_stack_m40 = 35;
        v_stack_m70 = (uint32_t)(result);
        result = v_stack_m70;
        Arg1 = *(uint64_t *)(v_rip + 0x3BCC56);
        result = v_stack_m58;
        v_stack_m80 = result;
        v_stack_m88 = 4;
        a4 = 0;
        result = EtwWriteTransfer(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4D268&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A4D268[BB_00A4D268]
  bb_00A4D297[BB_00A4D297]
  bb_00A4D338[BB_00A4D338]
  bb_00A4D34D[BB_00A4D34D]
  bb_00A4D268 -->|branch| bb_00A4D338
  bb_00A4D268 -->|fallthrough| bb_00A4D297
  bb_00A4D297 -->|flow| bb_00A4D338
```
