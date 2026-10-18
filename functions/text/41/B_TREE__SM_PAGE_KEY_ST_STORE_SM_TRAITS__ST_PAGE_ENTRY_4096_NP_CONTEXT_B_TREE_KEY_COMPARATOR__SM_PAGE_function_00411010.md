# B_TREE&lt;_SM_PAGE_KEY,ST_STORE&lt;SM_TRAITS&gt;::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR&lt;_SM_PAGE_KEY&gt; &gt;::BTreeIteratorCleanup

- RVA: `0x00411010`–`0x0041109A` (길이 `138` bytes)
- VA: `0x0000000140411010`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009BDAC`
- 디코드: `40`개 명령, `138/138` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00411059` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ST_STORE&lt;SM_TRAITS&gt;::StDmPageRemove](../20/ST_STORE_SM_TRAITS_StDmPageRemove_function_002049A0.md) at `0x00204C08`
- [sub_00410C73](Unknown_function_00410C73.md) at `0x00410C98`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmEtwPageRundown](../60/ST_STORE_SM_TRAITS_StDmEtwPageRundown_function_0060D544.md) at `0x0060D683`

### Static image references
- `0x0041102B` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0041108B` → [sub_006ED0C0](../6E/Unknown_function_006ED0C0.md) (`tail-transfer`)
  - `0x00411095` → [sub_006ED0C0](../6E/Unknown_function_006ED0C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00411010  40 55                           push rbp
00411012  48 83 EC 50                     sub rsp, 0x50
00411016  48 8D 6C 24 20                  lea rbp, [rsp + 0x20]
0041101B  48 89 5D 40                     mov qword ptr [rbp + 0x40], rbx
0041101F  48 89 75 48                     mov qword ptr [rbp + 0x48], rsi
00411023  48 89 7D 50                     mov qword ptr [rbp + 0x50], rdi
00411027  4C 89 75 58                     mov qword ptr [rbp + 0x58], r14
0041102B  48 8B 05 0E 97 9F 00            mov rax, qword ptr [rip + 0x9f970e]
00411032  48 33 C5                        xor rax, rbp
00411035  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
00411039  45 33 C0                        xor r8d, r8d
0041103C  48 8D 5A 10                     lea rbx, [rdx + 0x10]
00411040  48 85 D2                        test rdx, rdx
00411043  4C 8B F2                        mov r14, rdx
00411046  49 0F 44 D8                     cmove rbx, r8
0041104A  48 8B 03                        mov rax, qword ptr [rbx]
0041104D  83 38 FF                        cmp dword ptr [rax], -1
00411050  75 23                           jne 0x140411075
00411052  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00411056  48 33 CD                        xor rcx, rbp
00411059  E8 E2 B5 29 00                  call 0x1406ac640
0041105E  48 8B 5D 40                     mov rbx, qword ptr [rbp + 0x40]
00411062  48 8B 75 48                     mov rsi, qword ptr [rbp + 0x48]
00411066  48 8B 7D 50                     mov rdi, qword ptr [rbp + 0x50]
0041106A  4C 8B 75 58                     mov r14, qword ptr [rbp + 0x58]
0041106E  48 8D 65 30                     lea rsp, [rbp + 0x30]
00411072  5D                              pop rbp
00411073  C3                              ret
00411074  CC                              int3
00411075  48 8B 11                        mov rdx, qword ptr [rcx]
00411078  48 85 D2                        test rdx, rdx
0041107B  74 D5                           je 0x140411052
0041107D  49 8B 06                        mov rax, qword ptr [r14]
00411080  48 3B D0                        cmp rdx, rax
00411083  74 CD                           je 0x140411052
00411085  41 8B F0                        mov esi, r8d
00411088  48 85 C0                        test rax, rax
0041108B  0F 84 2F C0 2D 00               je 0x1406ed0c0
00411091  0F B6 70 02                     movzx esi, byte ptr [rax + 2]
00411095  E9 26 C0 2D 00                  jmp 0x1406ed0c0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (80);
    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_stack_p20 = v_r14;
    result = (*(unsigned __int64 *)(v_rip + 10458894)) ^ (v_stack_m38);
    v_stack_m10 = result;
    a3 = 0;
    v_rbx = a2 + 16;
    if (a2 == 0) { v_rbx = 0; }
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rbx))) != -1) goto loc_00411075;
loc_00411052:
    a1 = (v_stack_m10) ^ (v_stack_m38);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_00411075:
    if (*(unsigned __int64 *)(a1) == 0) goto loc_00411052;
    if ((*(unsigned __int64 *)(a1)) == (*(unsigned __int64 *)(v_stack_p20))) goto loc_00411052;
}
```

## 5. (Beta) C Style

```c
int64_t B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m38;
    uint64_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (80);
    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    v_stack_p20 = local_r14;
    result = (*(uint64_t *)(v_rip + 0x9F970E)) ^ (v_stack_m38);
    v_stack_m10 = result;
    Arg3 = 0;
    local_rbx = Arg2 + 16;
    if (Arg2 == NULL) { local_rbx = 0; }
    if ((*(uint32_t *)(*(uint64_t *)(local_rbx))) != -1) goto loc_00411075;
loc_00411052:
    Arg1 = (v_stack_m10) ^ (v_stack_m38);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    return result;
loc_00411075:
    if (*(uint64_t *)(arg1) == 0) goto loc_00411052;
    if ((*(uint64_t *)(arg1)) == (*(uint64_t *)(v_stack_p20))) goto loc_00411052;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00411010&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00411010[BB_00411010]
  bb_00411052[BB_00411052]
  bb_00411074[BB_00411074]
  bb_00411075[BB_00411075]
  bb_0041107D[BB_0041107D]
  bb_00411085[BB_00411085]
  bb_00411091[BB_00411091]
  bb_00411010 -->|branch| bb_00411075
  bb_00411010 -->|fallthrough| bb_00411052
  bb_00411074 -->|flow| bb_00411075
  bb_00411075 -->|branch| bb_00411052
  bb_00411075 -->|fallthrough| bb_0041107D
  bb_0041107D -->|branch| bb_00411052
  bb_0041107D -->|fallthrough| bb_00411085
  bb_00411085 -->|fallthrough| bb_00411091
```
