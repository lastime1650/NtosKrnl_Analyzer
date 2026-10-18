# TtmiLogSessionPowerRequestCreated

- RVA: `0x0077B41C`–`0x0077B4D4` (길이 `184` bytes)
- VA: `0x000000014077B41C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EA9C`
- 디코드: `42`개 명령, `184/184` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077B453` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077B4B9` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077B4C5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmNotifySessionPowerRequestCreated](TtmNotifySessionPowerRequestCreated_function_00776DD8.md) at `0x00776DF8`

### Static image references
- `0x0077B42A` → RVA `0x00E0A740` (`.data`; read)
- `0x0077B438` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077B48A` → RVA `0x00051230` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0077B453` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077B4B9` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077B4C5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077B41C  40 55                           push rbp
0077B41E  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
0077B423  48 81 EC A0 00 00 00            sub rsp, 0xa0
0077B42A  48 8B 05 0F F3 68 00            mov rax, qword ptr [rip + 0x68f30f]
0077B431  48 33 C4                        xor rax, rsp
0077B434  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0077B438  83 3D 89 D4 85 00 05            cmp dword ptr [rip + 0x85d489], 5
0077B43F  44 8B CA                        mov r9d, edx
0077B442  44 8B D1                        mov r10d, ecx
0077B445  76 77                           jbe 0x14077b4be
0077B447  BA 01 00 00 00                  mov edx, 1
0077B44C  48 8D 0D 75 D4 85 00            lea rcx, [rip + 0x85d475]
0077B453  E8 48 36 CB FF                  call 0x14042eaa0
0077B458  84 C0                           test al, al
0077B45A  74 62                           je 0x14077b4be
0077B45C  48 8D 45 EB                     lea rax, [rbp - 0x15]
0077B460  44 89 4D EF                     mov dword ptr [rbp - 0x11], r9d
0077B464  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0077B468  48 8D 0D 59 D4 85 00            lea rcx, [rip + 0x85d459]
0077B46F  48 8D 45 EF                     lea rax, [rbp - 0x11]
0077B473  44 88 45 E7                     mov byte ptr [rbp - 0x19], r8b
0077B477  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0077B47B  45 33 C9                        xor r9d, r9d
0077B47E  48 8D 45 E7                     lea rax, [rbp - 0x19]
0077B482  48 89 55 3F                     mov qword ptr [rbp + 0x3f], rdx
0077B486  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0077B48A  48 8D 15 9F 5D 8D FF            lea rdx, [rip - 0x72a261]
0077B491  48 8D 45 F7                     lea rax, [rbp - 9]
0077B495  44 89 55 EB                     mov dword ptr [rbp - 0x15], r10d
0077B499  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077B49E  45 33 C0                        xor r8d, r8d
0077B4A1  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
0077B4A9  48 C7 45 1F 04 00 00 00         mov qword ptr [rbp + 0x1f], 4
0077B4B1  48 C7 45 2F 04 00 00 00         mov qword ptr [rbp + 0x2f], 4
0077B4B9  E8 22 AC CA FF                  call 0x1404260e0
0077B4BE  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0077B4C2  48 33 CC                        xor rcx, rsp
0077B4C5  E8 76 11 F3 FF                  call 0x1406ac640
0077B4CA  48 81 C4 A0 00 00 00            add rsp, 0xa0
0077B4D1  5D                              pop rbp
0077B4D2  C3                              ret
0077B4D3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogSessionPowerRequestCreated(int a1, int a2, int a3)
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
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m74;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 6877967)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8770697)) <= 5) goto loc_0077B4BE;
    result = tlgKeywordOn(v_rip + 8770677, 1, a3, (unsigned int)(a2));
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m74;
        v_stack_m70 = (unsigned int)((unsigned int)(a2));
        v_stack_m48 = result;
        a1 = v_rip + 8770649;
        result = v_stack_m70;
        v_stack_m78 = (unsigned __int8)(a3);
        v_stack_m38 = result;
        a4 = 0;
        result = v_stack_m78;
        v_stack_m20 = 1;
        v_stack_m28 = result;
        a2 = v_rip - 7512673;
        result = v_stack_m68;
        v_stack_m74 = (unsigned int)((unsigned int)(a1));
        v_stack_m80 = result;
        a3 = 0;
        v_stack_m88 = 5;
        v_stack_m40 = 4;
        v_stack_m30 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogSessionPowerRequestCreated(int32_t Arg1, int32_t Arg2, int32_t Arg3)
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
    uint64_t v_stack_m5F;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m74;
    uint8_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x68F30F)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85D489)) <= 5) goto loc_0077B4BE;
    result = tlgKeywordOn(v_rip + 8770677, 1, Arg3, (uint32_t)(Arg2));
    if ((uint8_t)(result) != 0) {
        result = v_stack_m74;
        v_stack_m70 = (uint32_t)((uint32_t)(Arg2));
        v_stack_m48 = result;
        Arg1 = v_rip + 8770649;
        result = v_stack_m70;
        v_stack_m78 = (uint8_t)(Arg3);
        v_stack_m38 = result;
        a4 = 0;
        result = v_stack_m78;
        v_stack_m20 = 1;
        v_stack_m28 = result;
        Arg2 = v_rip - 7512673;
        result = v_stack_m68;
        v_stack_m74 = (uint32_t)((uint32_t)(Arg1));
        v_stack_m80 = result;
        Arg3 = 0;
        v_stack_m88 = 5;
        v_stack_m40 = 4;
        v_stack_m30 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077B41C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077B41C[BB_0077B41C]
  bb_0077B447[BB_0077B447]
  bb_0077B45C[BB_0077B45C]
  bb_0077B4BE[BB_0077B4BE]
  bb_0077B4D3[BB_0077B4D3]
  bb_0077B41C -->|branch| bb_0077B4BE
  bb_0077B41C -->|fallthrough| bb_0077B447
  bb_0077B447 -->|branch| bb_0077B4BE
  bb_0077B447 -->|fallthrough| bb_0077B45C
  bb_0077B45C -->|flow| bb_0077B4BE
```
