# B_TREE&lt;unsigned long,ST_STORE&lt;SM_TRAITS&gt;::_ST_HASH_ENTRY,4096,NP_CONTEXT,ST_STORE&lt;SM_TRAITS&gt;::ST_HASH_ENTRY_COMPARATOR&gt;::BTreeDescendToSibling

- RVA: `0x0060BB34`–`0x0060BB87` (길이 `83` bytes)
- VA: `0x000000014060BB34`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `28`개 명령, `83/83` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [B_TREE&lt;unsigned long,ST_STORE&lt;SM_TRAITS&gt;::_ST_HASH_ENTRY,4096,NP_CONTEXT,ST_STORE&lt;SM_TRAITS&gt;::ST_HASH_ENTRY_COMPARATOR&gt;::BTreeFindLeafSiblingEx](B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_HASH_EN_function_0060BB90.md) at `0x0060BBCE`
- [B_TREE&lt;unsigned long,ST_STORE&lt;SM_TRAITS&gt;::_ST_HASH_ENTRY,4096,NP_CONTEXT,ST_STORE&lt;SM_TRAITS&gt;::ST_HASH_ENTRY_COMPARATOR&gt;::BTreeFindLeafSiblingEx](B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_HASH_EN_function_0060BB90.md) at `0x0060BC5D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0060BB34  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
0060BB38  48 8B 11                        mov rdx, qword ptr [rcx]
0060BB3B  4D 85 C0                        test r8, r8
0060BB3E  74 15                           je 0x14060bb55
0060BB40  0F B6 42 02                     movzx eax, byte ptr [rdx + 2]
0060BB44  41 8B 48 18                     mov ecx, dword ptr [r8 + 0x18]
0060BB48  2B C8                           sub ecx, eax
0060BB4A  8B C1                           mov eax, ecx
0060BB4C  48 C1 E0 04                     shl rax, 4
0060BB50  49 03 00                        add rax, qword ptr [r8]
0060BB53  EB 02                           jmp 0x14060bb57
0060BB55  33 C0                           xor eax, eax
0060BB57  49 8D 49 08                     lea rcx, [r9 + 8]
0060BB5B  49 83 C1 10                     add r9, 0x10
0060BB5F  48 85 C0                        test rax, rax
0060BB62  74 0B                           je 0x14060bb6f
0060BB64  48 89 10                        mov qword ptr [rax], rdx
0060BB67  4C 89 48 08                     mov qword ptr [rax + 8], r9
0060BB6B  48 83 C0 10                     add rax, 0x10
0060BB6F  80 7A 02 02                     cmp byte ptr [rdx + 2], 2
0060BB73  74 0D                           je 0x14060bb82
0060BB75  48 8B 11                        mov rdx, qword ptr [rcx]
0060BB78  48 8D 4A 08                     lea rcx, [rdx + 8]
0060BB7C  4C 8D 4A 10                     lea r9, [rdx + 0x10]
0060BB80  EB DD                           jmp 0x14060bb5f
0060BB82  48 8B C1                        mov rax, rcx
0060BB85  C3                              ret
0060BB86  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    if (a3 == 0) goto loc_0060BB55;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 24))) - ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 2))));
    result = ((unsigned int)((unsigned int)(a1))) << (4);
    result = (result) + (*(unsigned __int64 *)(a3));
    goto loc_0060BB57;
loc_0060BB55:
    result = 0;
loc_0060BB57:
    a4 = (*(unsigned __int64 *)(a1 + 8)) + (16);
loc_0060BB5F:
    if (0 != 0) {
        *(unsigned __int64 *)(result) = *(unsigned __int64 *)(a1);
        *(unsigned __int64 *)(result + 8) = a4;
        result = (result) + (16);
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 2)) == 2) goto loc_0060BB82;
    goto loc_0060BB5F;
loc_0060BB82:
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 8;
}
```

## 5. (Beta) C Style

```c
int64_t B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_HASH_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_HAS(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (Arg3 == 0) goto loc_0060BB55;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x18))) - ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1) + 0x2))));
    result = ((uint32_t)((uint32_t)(Arg1))) << (4);
    result = (result) + (*(uint64_t *)(Arg3));
    goto loc_0060BB57;
loc_0060BB55:
    result = 0;
loc_0060BB57:
    a4 = (*(uint64_t *)(arg1 + 0x8)) + (16);
loc_0060BB5F:
    if (0 != 0) {
        *(uint64_t *)(result) = *(uint64_t *)(arg1);
        *(uint64_t *)(result + 0x8) = a4;
        result = (result) + (16);
    }
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x2)) == 2) goto loc_0060BB82;
    goto loc_0060BB5F;
loc_0060BB82:
    return *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0060BB34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0060BB34[BB_0060BB34]
  bb_0060BB40[BB_0060BB40]
  bb_0060BB55[BB_0060BB55]
  bb_0060BB57[BB_0060BB57]
  bb_0060BB5F[BB_0060BB5F]
  bb_0060BB64[BB_0060BB64]
  bb_0060BB6F[BB_0060BB6F]
  bb_0060BB75[BB_0060BB75]
  bb_0060BB82[BB_0060BB82]
  bb_0060BB86[BB_0060BB86]
  bb_0060BB34 -->|branch| bb_0060BB55
  bb_0060BB34 -->|fallthrough| bb_0060BB40
  bb_0060BB40 -->|branch| bb_0060BB57
  bb_0060BB55 -->|flow| bb_0060BB57
  bb_0060BB57 -->|flow| bb_0060BB5F
  bb_0060BB5F -->|branch| bb_0060BB6F
  bb_0060BB5F -->|fallthrough| bb_0060BB64
  bb_0060BB64 -->|flow| bb_0060BB6F
  bb_0060BB6F -->|branch| bb_0060BB82
  bb_0060BB6F -->|fallthrough| bb_0060BB75
  bb_0060BB75 -->|branch| bb_0060BB5F
```
