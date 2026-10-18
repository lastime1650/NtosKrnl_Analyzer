# PopTraceNetRefreshTimerArmed

- RVA: `0x00763CD4`–`0x00763D73` (길이 `159` bytes)
- VA: `0x0000000140763CD4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A06A8`
- 디코드: `35`개 명령, `159/159` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00763D03` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00763D5A` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00763D67` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopNetArmRefreshTimer](PopNetArmRefreshTimer_function_007689D0.md) at `0x00768A22`

### Static image references
- `0x00763CDA` → RVA `0x00E0A740` (`.data`; read)
- `0x00763CE9` → RVA `0x00E67858` (`.data`; read)
- `0x00763CF5` → RVA `0x00F0B408` (`.data`; read)
- `0x00763CFC` → RVA `0x00022CD8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00763D03` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00763D5A` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00763D67` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00763CD4  40 53                           push rbx
00763CD6  48 83 EC 50                     sub rsp, 0x50
00763CDA  48 8B 05 5F 6A 6A 00            mov rax, qword ptr [rip + 0x6a6a5f]
00763CE1  48 33 C4                        xor rax, rsp
00763CE4  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00763CE9  80 3D 68 3B 70 00 00            cmp byte ptr [rip + 0x703b68], 0
00763CF0  48 8B D9                        mov rbx, rcx
00763CF3  74 6A                           je 0x140763d5f
00763CF5  48 8B 0D 0C 77 7A 00            mov rcx, qword ptr [rip + 0x7a770c]
00763CFC  48 8D 15 D5 EF 8B FF            lea rdx, [rip - 0x74102b]
00763D03  E8 48 E7 C2 FF                  call 0x140392450
00763D08  84 C0                           test al, al
00763D0A  74 53                           je 0x140763d5f
00763D0C  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
00763D11  48 B8 CD CC CC CC CC CC CC CC   movabs rax, 0xcccccccccccccccd
00763D1B  48 8B 0D E6 76 7A 00            mov rcx, qword ptr [rip + 0x7a76e6]
00763D22  41 B9 01 00 00 00               mov r9d, 1
00763D28  48 F7 E3                        mul rbx
00763D2B  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00763D30  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
00763D38  48 C1 EA 03                     shr rdx, 3
00763D3C  45 33 C0                        xor r8d, r8d
00763D3F  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00763D44  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00763D49  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00763D4E  48 8D 15 83 EF 8B FF            lea rdx, [rip - 0x74107d]
00763D55  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00763D5A  E8 C1 89 CB FF                  call 0x14041c720
00763D5F  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00763D64  48 33 CC                        xor rcx, rsp
00763D67  E8 D4 88 F4 FF                  call 0x1406ac640
00763D6C  48 83 C4 50                     add rsp, 0x50
00763D70  5B                              pop rbx
00763D71  C3                              ret
00763D72  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopTraceNetRefreshTimerArmed(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (80);
    result = (*(unsigned __int64 *)(v_rip + 6974047)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned __int8 *)(v_rip + 7355240)) == 0) goto loc_00763D5F;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8025868), v_rip - 7606315, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 8025830);
        a4 = 1;
        result = v_stack_m28;
        v_stack_m18 = 8;
        a2 = (v_rip - 7606315) >> (3);
        a3 = 0;
        v_stack_m20 = result;
        result = v_stack_m20;
        v_stack_m28 = a2;
        a2 = v_rip - 7606397;
        v_stack_m38 = result;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopTraceNetRefreshTimerArmed(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (80);
    result = (*(uint64_t *)(v_rip + 0x6A6A5F)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint8_t *)(v_rip + 0x703B68)) == 0) goto loc_00763D5F;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7A770C), v_rip - 7606315, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x7A76E6);
        a4 = 1;
        result = v_stack_m28;
        v_stack_m18 = 8;
        Arg2 = (v_rip - 7606315) >> (3);
        Arg3 = 0;
        v_stack_m20 = result;
        result = v_stack_m20;
        v_stack_m28 = Arg2;
        Arg2 = v_rip - 7606397;
        v_stack_m38 = result;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (80);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00763CD4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00763CD4[BB_00763CD4]
  bb_00763CF5[BB_00763CF5]
  bb_00763D0C[BB_00763D0C]
  bb_00763D5F[BB_00763D5F]
  bb_00763D72[BB_00763D72]
  bb_00763CD4 -->|branch| bb_00763D5F
  bb_00763CD4 -->|fallthrough| bb_00763CF5
  bb_00763CF5 -->|branch| bb_00763D5F
  bb_00763CF5 -->|fallthrough| bb_00763D0C
  bb_00763D0C -->|flow| bb_00763D5F
```
