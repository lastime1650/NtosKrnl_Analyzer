# sub_00B18ADC

- RVA: `0x00B18ADC`–`0x00B18AF5` (길이 `25` bytes)
- VA: `0x0000000140B18ADC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007C064`
- 디코드: `5`개 명령, `25/25` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B18AF0` → [PspSetJobLimitsJobPreCallback + 0x1C](../87/PspSetJobLimitsJobPreCallback_function_0087E6C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B18ADC  48 85 FF                        test rdi, rdi
00B18ADF  74 04                           je 0x140b18ae5
00B18AE1  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
00B18AE5  F0 81 8B 10 06 00 00 00 01 00 00  lock or dword ptr [rbx + 0x610], 0x100
00B18AF0  E9 E7 5B D6 FF                  jmp 0x14087e6dc
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00B18ADC(void)
{
    if (v_rdi != 0) {
        *(unsigned __int8 *)(v_rdi + 10) = 1;
    }
}
```

## 5. (Beta) C Style

```c
void sub_00B18ADC(void)
{
    if (local_rdi != 0) {
        *(uint8_t *)(local_rdi + 0xA) = 1;
    }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B18ADC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B18ADC[BB_00B18ADC]
  bb_00B18AE1[BB_00B18AE1]
  bb_00B18AE5[BB_00B18AE5]
  bb_00B18ADC -->|branch| bb_00B18AE5
  bb_00B18ADC -->|fallthrough| bb_00B18AE1
  bb_00B18AE1 -->|flow| bb_00B18AE5
```
