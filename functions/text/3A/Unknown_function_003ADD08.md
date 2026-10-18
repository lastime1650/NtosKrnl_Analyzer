# sub_003ADD08

- RVA: `0x003ADD08`–`0x003ADD4D` (길이 `69` bytes)
- VA: `0x00000001403ADD08`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008BE58`
- 디코드: `18`개 명령, `69/69` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003ADD24` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x003ADD43` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeDeleteNode](B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AA598.md) (function, `0x003AA598`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x003ADD0C` → [sub_003ADBE7 + 0x8](Unknown_function_003ADBE7.md) (`tail-transfer`)
  - `0x003ADD34` → [sub_003ADD5D](Unknown_function_003ADD5D.md) (`tail-transfer`)
  - `0x003ADD48` → [sub_003ADBE7 + 0x8](Unknown_function_003ADBE7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003ADD08  80 7B 03 00                     cmp byte ptr [rbx + 3], 0
003ADD0C  0F 85 DD FE FF FF               jne 0x1403adbef
003ADD12  45 8B 45 1C                     mov r8d, dword ptr [r13 + 0x1c]
003ADD16  48 8D 57 10                     lea rdx, [rdi + 0x10]
003ADD1A  41 FF C8                        dec r8d
003ADD1D  48 8B CF                        mov rcx, rdi
003ADD20  49 C1 E0 04                     shl r8, 4
003ADD24  E8 17 8B 31 00                  call 0x1406c6840
003ADD29  41 FF 4D 18                     dec dword ptr [r13 + 0x18]
003ADD2D  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
003ADD31  83 38 FF                        cmp dword ptr [rax], -1
003ADD34  75 27                           jne 0x1403add5d
003ADD36  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
003ADD3A  48 89 06                        mov qword ptr [rsi], rax
003ADD3D  48 8B D3                        mov rdx, rbx
003ADD40  48 8B CE                        mov rcx, rsi
003ADD43  E8 50 C8 FF FF                  call 0x1403aa598
003ADD48  E9 A2 FE FF FF                  jmp 0x1403adbef
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003ADD08(void)
{
    __int64 result;

    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r13 + 28))) - 1);
    a3 = (a3) << (4);
    result = memcpy(v_rdi, v_rdi + 16, a3, a4);
    *(unsigned __int64 *)(v_rsi) = *(unsigned __int64 *)(v_rbx + 8);
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(v_rsi, v_rbx, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_003ADD08(void)
{
    int64_t result;

    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r13 + 0x1C))) - 1);
    a3 = (a3) << (4);
    result = memcpy(local_rdi, local_rdi + 16, a3, a4);
    *(uint64_t *)(local_rsi) = *(uint64_t *)(local_rbx + 0x8);
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(local_rsi, local_rbx, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003ADD08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003ADD08[BB_003ADD08]
  bb_003ADD12[BB_003ADD12]
  bb_003ADD36[BB_003ADD36]
  bb_003ADD08 -->|fallthrough| bb_003ADD12
  bb_003ADD12 -->|fallthrough| bb_003ADD36
```
