# sub_006DF27C

- RVA: `0x006DF27C`–`0x006DF29A` (길이 `30` bytes)
- VA: `0x00000001406DF27C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000721FC`
- 디코드: `6`개 명령, `30/30` bytes 표시
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
  - `0x006DF280` → [RtlInitializeExtendedContext2 + 0x6B](../2F/RtlInitializeExtendedContext2_function_002F5D40.md) (`tail-transfer`)
  - `0x006DF295` → [RtlInitializeExtendedContext2 + 0x62](../2F/RtlInitializeExtendedContext2_function_002F5D40.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DF27C  0F BA E7 16                     bt edi, 0x16
006DF280  0F 83 25 6B C1 FF               jae 0x1402f5dab
006DF286  48 8D 4E 0F                     lea rcx, [rsi + 0xf]
006DF28A  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
006DF28E  48 8D 99 90 03 00 00            lea rbx, [rcx + 0x390]
006DF295  E9 08 6B C1 FF                  jmp 0x1402f5da2
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006DF27C(void)
{
    a1 = (v_rsi + 15) & (-16);
}
```

## 5. (Beta) C Style

```c
void sub_006DF27C(void)
{
    a1 = (local_rsi + 15) & (-16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DF27C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DF27C[BB_006DF27C]
  bb_006DF286[BB_006DF286]
  bb_006DF27C -->|fallthrough| bb_006DF286
```
