# sub_006EACF8

- RVA: `0x006EACF8`–`0x006EAD16` (길이 `30` bytes)
- VA: `0x00000001406EACF8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00095994`
- 디코드: `7`개 명령, `30/30` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x006EAD01` → [MiPartitionObjectToPartition + 0x46](../3E/MiPartitionObjectToPartition_function_003EAB0C.md) (`tail-transfer`)
  - `0x006EAD09` → [MiPartitionObjectToPartition + 0x7C](../3E/MiPartitionObjectToPartition_function_003EAB0C.md) (`tail-transfer`)
  - `0x006EAD11` → [MiPartitionObjectToPartition + 0x7C](../3E/MiPartitionObjectToPartition_function_003EAB0C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006EACF8  41 BB 01 00 00 00               mov r11d, 1
006EACFE  4D 8B D0                        mov r10, r8
006EAD01  E9 4C FE CF FF                  jmp 0x1403eab52
006EAD06  4D 8B D1                        mov r10, r9
006EAD09  E9 7A FE CF FF                  jmp 0x1403eab88
006EAD0E  41 B1 01                        mov r9b, 1
006EAD11  E9 72 FE CF FF                  jmp 0x1403eab88
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006EACF8(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
}
```

## 5. (Beta) C Style

```c
void sub_006EACF8(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006EACF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006EACF8[BB_006EACF8]
  bb_006EAD06[BB_006EAD06]
  bb_006EAD0E[BB_006EAD0E]
```
