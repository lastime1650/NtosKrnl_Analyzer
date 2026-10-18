# sub_006E7B00

- RVA: `0x006E7B00`–`0x006E7B1A` (길이 `26` bytes)
- VA: `0x00000001406E7B00`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008CB64`
- 디코드: `6`개 명령, `26/26` bytes 표시
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
  - `0x006E7B08` → [MmQueryMemoryListInformation + 0x9F](../3B/MmQueryMemoryListInformation_function_003B9EDC.md) (`tail-transfer`)
  - `0x006E7B15` → [MmQueryMemoryListInformation + 0xC2](../3B/MmQueryMemoryListInformation_function_003B9EDC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E7B00  48 8B 1F                        mov rbx, qword ptr [rdi]
006E7B03  BA 01 00 00 00                  mov edx, 1
006E7B08  E9 6E 24 CD FF                  jmp 0x1403b9f7b
006E7B0D  40 B6 01                        mov sil, 1
006E7B10  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
006E7B15  E9 84 24 CD FF                  jmp 0x1403b9f9e
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006E7B00(void)
{
    unsigned __int8 v_stack_p30;
}
```

## 5. (Beta) C Style

```c
void sub_006E7B00(void)
{
    uint8_t v_stack_p30;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E7B00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E7B00[BB_006E7B00]
  bb_006E7B0D[BB_006E7B0D]
```
