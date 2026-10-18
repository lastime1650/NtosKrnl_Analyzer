# sub_00B326BC

- RVA: `0x00B326BC`–`0x00B326DB` (길이 `31` bytes)
- VA: `0x0000000140B326BC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A7280`
- 디코드: `8`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B326D0` → [EtwpUpdateEventFilterAndFree](../70/EtwpUpdateEventFilterAndFree_function_00700B94.md) (function, `0x00700B94`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B326D6` → [EtwpUpdateGuidFilterData + 0x214](../9F/EtwpUpdateGuidFilterData_function_009FD214.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B326BC  8B C7                           mov eax, edi
00B326BE  48 6B C8 68                     imul rcx, rax, 0x68
00B326C2  49 8B 87 80 02 00 00            mov rax, qword ptr [r15 + 0x280]
00B326C9  48 83 C0 58                     add rax, 0x58
00B326CD  48 03 C8                        add rcx, rax
00B326D0  E8 BF E4 BC FF                  call 0x140700b94
00B326D5  90                              nop
00B326D6  E9 4D AD EC FF                  jmp 0x1409fd428
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B326BC(void)
{
    __int64 result;

    a1 = (a1) * ((unsigned int)((unsigned int)(v_rdi)));
    result = (*(unsigned __int64 *)(v_r15 + 640)) + (88);
    a1 = (a1) + (result);
    result = EtwpUpdateEventFilterAndFree(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B326BC(void)
{
    int64_t result;

    a1 = (a1) * ((uint32_t)((uint32_t)(local_rdi)));
    result = (*(uint64_t *)(local_r15 + 0x280)) + (88);
    a1 = (a1) + (result);
    result = EtwpUpdateEventFilterAndFree(a1, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B326BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B326BC[BB_00B326BC]
```
