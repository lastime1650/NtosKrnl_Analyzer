# sub_006EEE2E

- RVA: `0x006EEE2E`–`0x006EEE47` (길이 `25` bytes)
- VA: `0x00000001406EEE2E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A2CE4`
- 디코드: `6`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006EEE31` → [sub_004358F7 + 0x5](../43/Unknown_function_004358F7.md) (`tail-transfer`)
  - `0x006EEE42` → [sub_004358F7 + 0x14](../43/Unknown_function_004358F7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006EEE2E  48 3B DD                        cmp rbx, rbp
006EEE31  0F 85 C5 6A D4 FF               jne 0x1404358fc
006EEE37  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
006EEE3B  49 23 CD                        and rcx, r13
006EEE3E  48 89 4B 28                     mov qword ptr [rbx + 0x28], rcx
006EEE42  E9 C4 6A D4 FF                  jmp 0x14043590b
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006EEE2E(void)
{
    a1 = (*(unsigned __int64 *)(v_rbx + 40)) & (v_r13);
    *(unsigned __int64 *)(v_rbx + 40) = a1;
}
```

## 5. (Beta) C Style

```c
void sub_006EEE2E(void)
{
    a1 = (*(uint64_t *)(local_rbx + 0x28)) & (local_r13);
    *(uint64_t *)(local_rbx + 0x28) = a1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006EEE2E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006EEE2E[BB_006EEE2E]
  bb_006EEE37[BB_006EEE37]
  bb_006EEE2E -->|fallthrough| bb_006EEE37
```
