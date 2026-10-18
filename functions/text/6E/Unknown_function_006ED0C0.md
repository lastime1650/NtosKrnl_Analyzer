# sub_006ED0C0

- RVA: `0x006ED0C0`–`0x006ED15F` (길이 `159` bytes)
- VA: `0x00000001406ED0C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009BDD4`
- 디코드: `40`개 명령, `159/159` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006ED0E0` → [_chkstk](../6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x006ED112` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchKey](../3A/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AC3C0.md) (function, `0x003AC3C0`)
- `0x006ED12D` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchResultDeref](../3A/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AC5D0.md) (function, `0x003AC5D0`)
- `0x006ED154` → [NP_CONTEXT::NpLeafDerefInternal](../3A/NP_CONTEXT_NpLeafDerefInternal_function_003A9A70.md) (function, `0x003A9A70`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006ED14B` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeIteratorCleanup + 0x42](../41/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_00411010.md) (`tail-transfer`)
  - `0x006ED15A` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeIteratorCleanup + 0x42](../41/B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_00411010.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006ED0C0  8B C6                           mov eax, esi
006ED0C2  48 C1 E0 04                     shl rax, 4
006ED0C6  48 8D 48 0F                     lea rcx, [rax + 0xf]
006ED0CA  48 3B C8                        cmp rcx, rax
006ED0CD  77 0A                           ja 0x1406ed0d9
006ED0CF  48 B9 F0 FF FF FF FF FF FF 0F   movabs rcx, 0xffffffffffffff0
006ED0D9  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
006ED0DD  48 8B C1                        mov rax, rcx
006ED0E0  E8 7B D8 FC FF                  call 0x1406ba960
006ED0E5  8B 52 10                        mov edx, dword ptr [rdx + 0x10]
006ED0E8  48 2B E1                        sub rsp, rcx
006ED0EB  0F 57 C0                        xorps xmm0, xmm0
006ED0EE  44 89 45 18                     mov dword ptr [rbp + 0x18], r8d
006ED0F2  4C 8D 45 00                     lea r8, [rbp]
006ED0F6  48 C7 45 20 01 00 00 00         mov qword ptr [rbp + 0x20], 1
006ED0FE  49 8B CE                        mov rcx, r14
006ED101  89 75 1C                        mov dword ptr [rbp + 0x1c], esi
006ED104  48 8D 7C 24 20                  lea rdi, [rsp + 0x20]
006ED109  48 89 7D 00                     mov qword ptr [rbp], rdi
006ED10D  F3 0F 7F 45 08                  movdqu xmmword ptr [rbp + 8], xmm0
006ED112  E8 A9 F2 CB FF                  call 0x1403ac3c0
006ED117  8D 4E FE                        lea ecx, [rsi - 2]
006ED11A  48 03 C9                        add rcx, rcx
006ED11D  48 8D 55 00                     lea rdx, [rbp]
006ED121  48 8B 74 CF 08                  mov rsi, qword ptr [rdi + rcx*8 + 8]
006ED126  48 8B 3C CF                     mov rdi, qword ptr [rdi + rcx*8]
006ED12A  49 8B CE                        mov rcx, r14
006ED12D  E8 9E F4 CB FF                  call 0x1403ac5d0
006ED132  48 8D 47 08                     lea rax, [rdi + 8]
006ED136  48 8D 4F 10                     lea rcx, [rdi + 0x10]
006ED13A  48 3B F1                        cmp rsi, rcx
006ED13D  48 8D 56 F8                     lea rdx, [rsi - 8]
006ED141  48 0F 46 D0                     cmovbe rdx, rax
006ED145  48 8B 03                        mov rax, qword ptr [rbx]
006ED148  83 38 FF                        cmp dword ptr [rax], -1
006ED14B  0F 84 01 3F D2 FF               je 0x140411052
006ED151  48 8B CB                        mov rcx, rbx
006ED154  E8 17 C9 CB FF                  call 0x1403a9a70
006ED159  90                              nop
006ED15A  E9 F3 3E D2 FF                  jmp 0x140411052
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006ED0C0(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;

    result = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    if ((result + 15) <= result) {
    }
    a1 = (result + 15) & (-16);
    result = _chkstk(a1, a2, a3, a4);
    v_rsp = (v_rsp) - (a1);
    *(unsigned int *)(v_rbp + 24) = a3;
    *(unsigned __int64 *)(v_rbp + 32) = 1;
    *(unsigned int *)(v_rbp + 28) = (unsigned int)(v_rsi);
    *(unsigned __int64 *)(v_rbp) = v_stack_p20;
    *(unsigned __int64 *)(v_rbp + 8) = v_xmm0;
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(v_r14, (unsigned int)(*(unsigned int *)(a2 + 16)), v_rbp, a4);
    a1 = (v_rsi - 2) + (v_rsi - 2);
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(v_r14, v_rbp, v_rbp, a4);
    a2 = *(unsigned __int64 *)(v_stack_p20 + a1 * 8 + 8) - 8;
    if ((*(unsigned __int64 *)(v_stack_p20 + a1 * 8 + 8)) <= (*(unsigned __int64 *)(v_stack_p20 + a1 * 8) + 16)) { a2 = *(unsigned __int64 *)(v_stack_p20 + a1 * 8) + 8; }
    result = NP_CONTEXT__NpLeafDerefInternal(v_rbx, a2, v_rbp, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006ED0C0(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;

    result = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    if ((result + 15) <= result) {
    }
    Arg1 = (result + 15) & (-16);
    result = _chkstk(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) - (Arg1);
    *(uint32_t *)(local_rbp + 0x18) = Arg3;
    *(uint64_t *)(local_rbp + 0x20) = 1;
    *(uint32_t *)(local_rbp + 0x1C) = (uint32_t)(local_rsi);
    *(uint64_t *)(local_rbp) = v_stack_p20;
    *(uint64_t *)(local_rbp + 0x8) = v_xmm0;
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(local_r14, (uint32_t)(*(uint32_t *)(Arg2 + 0x10)), local_rbp, a4);
    Arg1 = (local_rsi - 2) + (local_rsi - 2);
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(local_r14, local_rbp, local_rbp, a4);
    Arg2 = *(uint64_t *)(v_stack_p20 + Arg1 * 8 + 0x8) - 8;
    if ((*(uint64_t *)(v_stack_p20 + Arg1 * 8 + 0x8)) <= (*(uint64_t *)(v_stack_p20 + Arg1 * 8) + 16)) { Arg2 = *(uint64_t *)(v_stack_p20 + Arg1 * 8) + 8; }
    result = NP_CONTEXT__NpLeafDerefInternal(local_rbx, Arg2, local_rbp, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006ED0C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006ED0C0[BB_006ED0C0]
  bb_006ED0CF[BB_006ED0CF]
  bb_006ED0D9[BB_006ED0D9]
  bb_006ED151[BB_006ED151]
  bb_006ED0C0 -->|branch| bb_006ED0D9
  bb_006ED0C0 -->|fallthrough| bb_006ED0CF
  bb_006ED0CF -->|flow| bb_006ED0D9
  bb_006ED0D9 -->|fallthrough| bb_006ED151
```
