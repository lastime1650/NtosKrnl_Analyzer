# sub_003AE62C

- RVA: `0x003AE62C`–`0x003AE671` (길이 `69` bytes)
- VA: `0x00000001403AE62C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008BF80`
- 디코드: `18`개 명령, `69/69` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003AE648` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x003AE667` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeDeleteNode](B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AA598.md) (function, `0x003AA598`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x003AE630` → [sub_003AE4BD + 0x20](Unknown_function_003AE4BD.md) (`tail-transfer`)
  - `0x003AE658` → [sub_003AE68A](Unknown_function_003AE68A.md) (`tail-transfer`)
  - `0x003AE66C` → [sub_003AE4BD + 0x20](Unknown_function_003AE4BD.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003AE62C  80 7B 03 00                     cmp byte ptr [rbx + 3], 0
003AE630  0F 85 A7 FE FF FF               jne 0x1403ae4dd
003AE636  45 8B 45 1C                     mov r8d, dword ptr [r13 + 0x1c]
003AE63A  48 8D 57 10                     lea rdx, [rdi + 0x10]
003AE63E  41 FF C8                        dec r8d
003AE641  48 8B CF                        mov rcx, rdi
003AE644  49 C1 E0 04                     shl r8, 4
003AE648  E8 F3 81 31 00                  call 0x1406c6840
003AE64D  41 FF 4D 18                     dec dword ptr [r13 + 0x18]
003AE651  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
003AE655  83 38 FF                        cmp dword ptr [rax], -1
003AE658  75 30                           jne 0x1403ae68a
003AE65A  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
003AE65E  48 89 06                        mov qword ptr [rsi], rax
003AE661  48 8B D3                        mov rdx, rbx
003AE664  48 8B CE                        mov rcx, rsi
003AE667  E8 2C BF FF FF                  call 0x1403aa598
003AE66C  E9 6C FE FF FF                  jmp 0x1403ae4dd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003AE62C(void)
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
void sub_003AE62C(void)
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003AE62C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003AE62C[BB_003AE62C]
  bb_003AE636[BB_003AE636]
  bb_003AE65A[BB_003AE65A]
  bb_003AE62C -->|fallthrough| bb_003AE636
  bb_003AE636 -->|fallthrough| bb_003AE65A
```
