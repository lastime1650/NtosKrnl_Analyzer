# sub_006DC9A8

- RVA: `0x006DC9A8`–`0x006DC9C5` (길이 `29` bytes)
- VA: `0x00000001406DC9A8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EF58`
- 디코드: `8`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DC9BA` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006DC9B2` → [PspIumReplenishPartitionPages + 0xD5](../2C/PspIumReplenishPartitionPages_function_002C8710.md) (`tail-transfer`)
  - `0x006DC9C0` → [PspIumReplenishPartitionPages + 0x53](../2C/PspIumReplenishPartitionPages_function_002C8710.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DC9A8  40 0F B6 C6                     movzx eax, sil
006DC9AC  44 0F 22 C0                     mov cr8, rax
006DC9B0  B0 01                           mov al, 1
006DC9B2  E9 2E BE BE FF                  jmp 0x1402c87e5
006DC9B7  48 8B CD                        mov rcx, rbp
006DC9BA  E8 C1 C4 B6 FF                  call 0x140248e80
006DC9BF  90                              nop
006DC9C0  E9 9E BD BE FF                  jmp 0x1402c8763
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DC9A8(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_006DC9A8(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DC9A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DC9A8[BB_006DC9A8]
  bb_006DC9B7[BB_006DC9B7]
```
