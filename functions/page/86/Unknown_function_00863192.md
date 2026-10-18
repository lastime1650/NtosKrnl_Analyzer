# sub_00863192

- RVA: `0x00863192`–`0x008631B3` (길이 `33` bytes)
- VA: `0x0000000140863192`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B7B0`
- 디코드: `8`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00863195` → [CmpLockDeletedHashEntryExclusiveByKcb](../9B/CmpLockDeletedHashEntryExclusiveByKcb_function_009B3030.md) (function, `0x009B3030`)
- `0x008631A1` → [CmpRemoveKeyHashFromDeletedKcbTable](../9E/CmpRemoveKeyHashFromDeletedKcbTable_function_009EC364.md) (function, `0x009EC364`)
- `0x008631A9` → [CmpUnlockDeletedHashEntryByKcb](../9B/CmpUnlockDeletedHashEntryByKcb_function_009B3100.md) (function, `0x009B3100`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008631AE` → [sub_00862DAA + 0x69](Unknown_function_00862DAA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00863192  48 8B CB                        mov rcx, rbx
00863195  E8 96 FE 14 00                  call 0x1409b3030
0086319A  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
0086319E  49 8B D6                        mov rdx, r14
008631A1  E8 BE 91 18 00                  call 0x1409ec364
008631A6  48 8B CB                        mov rcx, rbx
008631A9  E8 52 FF 14 00                  call 0x1409b3100
008631AE  E9 60 FC FF FF                  jmp 0x140862e13
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00863192(void)
{
    __int64 result;

    result = CmpLockDeletedHashEntryExclusiveByKcb(v_rbx, a2, a3, a4);
    result = CmpRemoveKeyHashFromDeletedKcbTable(*(unsigned __int64 *)(v_rbx + 32), v_r14, a3, a4);
    result = CmpUnlockDeletedHashEntryByKcb(v_rbx, v_r14, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00863192(void)
{
    int64_t result;

    result = CmpLockDeletedHashEntryExclusiveByKcb(local_rbx, a2, a3, a4);
    result = CmpRemoveKeyHashFromDeletedKcbTable(*(uint64_t *)(local_rbx + 0x20), local_r14, a3, a4);
    result = CmpUnlockDeletedHashEntryByKcb(local_rbx, local_r14, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00863192&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00863192[BB_00863192]
```
