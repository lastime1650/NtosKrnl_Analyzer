# CmpTraceHiveFlushStop

- RVA: `0x009B4920`–`0x009B49A9` (길이 `137` bytes)
- VA: `0x00000001409B4920`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CABC`
- 디코드: `30`개 명령, `137/137` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009B4950` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x009B4961` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009B49A2` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)

### Direct callers
- [CmpFlushHive](CmpFlushHive_function_009B3DC0.md) at `0x009B3FE4`

### Static image references
- `0x009B4928` → RVA `0x00E0A740` (`.data`; read)
- `0x009B4937` → RVA `0x00013C30` (`.rdata`; read)
- `0x009B493E` → RVA `0x00FD8018` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009B4950` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x009B4961` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009B49A2` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009B4920  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
009B4924  48 83 EC 68                     sub rsp, 0x68
009B4928  48 8B 05 11 5E 45 00            mov rax, qword ptr [rip + 0x455e11]
009B492F  48 33 C4                        xor rax, rsp
009B4932  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009B4937  0F 10 05 F2 F2 65 FF            movups xmm0, xmmword ptr [rip - 0x9a0d0e]
009B493E  48 8B 0D D3 36 62 00            mov rcx, qword ptr [rip + 0x6236d3]
009B4945  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
009B494A  F3 0F 7F 44 24 30               movdqu xmmword ptr [rsp + 0x30], xmm0
009B4950  E8 FB DA 9D FF                  call 0x140392450
009B4955  84 C0                           test al, al
009B4957  75 13                           jne 0x1409b496c
009B4959  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
009B495E  48 33 CC                        xor rcx, rsp
009B4961  E8 DA 7C CF FF                  call 0x1406ac640
009B4966  48 83 C4 68                     add rsp, 0x68
009B496A  C3                              ret
009B496B  CC                              int3
009B496C  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
009B4971  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009B4976  48 8B 0D 9B 36 62 00            mov rcx, qword ptr [rip + 0x62369b]
009B497D  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
009B4982  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009B4987  41 B9 01 00 00 00               mov r9d, 1
009B498D  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009B4992  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
009B499A  45 33 C0                        xor r8d, r8d
009B499D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009B49A2  E8 79 7D A6 FF                  call 0x14041c720
009B49A7  EB B0                           jmp 0x1409b4959
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTraceHiveFlushStop(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 4546065)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m38 = v_xmm0;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6436563), v_stack_m38, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009B496C;
loc_009B4959:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m38, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
loc_009B496C:
    v_stack_p40 = v_stack_p70;
    v_stack_p48 = 4;
    a3 = 0;
    v_stack_p20 = v_stack_p40;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 6436507), v_stack_p30, a3, 1);
    goto loc_009B4959;
}
```

## 5. (Beta) C Style

```c
int64_t CmpTraceHiveFlushStop(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m38;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint64_t v_stack_p70;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x455E11)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m38 = v_xmm0;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x6236D3), v_stack_m38, Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_009B496C;
loc_009B4959:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m38, Arg3, a4);
    local_rsp = (local_rsp) + (104);
    return result;
loc_009B496C:
    v_stack_p40 = v_stack_p70;
    v_stack_p48 = 4;
    Arg3 = 0;
    v_stack_p20 = v_stack_p40;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x62369B), v_stack_p30, Arg3, 1);
    goto loc_009B4959;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009B4920&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009B4920[BB_009B4920]
  bb_009B4959[BB_009B4959]
  bb_009B496B[BB_009B496B]
  bb_009B496C[BB_009B496C]
  bb_009B4920 -->|branch| bb_009B496C
  bb_009B4920 -->|fallthrough| bb_009B4959
  bb_009B496B -->|flow| bb_009B496C
  bb_009B496C -->|branch| bb_009B4959
```
