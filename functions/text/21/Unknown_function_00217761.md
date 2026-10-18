# sub_00217761

- RVA: `0x00217761`–`0x00217780` (길이 `31` bytes)
- VA: `0x0000000140217761`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005E62C`
- 디코드: `6`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00217776` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0021776A` → [sub_002175E7 + 0xD8](Unknown_function_002175E7.md) (`tail-transfer`)
  - `0x0021777B` → [sub_002175E7 + 0x52](Unknown_function_002175E7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00217761  F0 41 81 65 00 7F FF FF FF      lock and dword ptr [r13], 0xffffff7f
0021776A  E9 50 FF FF FF                  jmp 0x1402176bf
0021776F  0F B6 D0                        movzx edx, al
00217772  40 0F B6 CE                     movzx ecx, sil
00217776  E8 81 DF 2D 00                  call 0x1404f56fc
0021777B  E9 B9 FE FF FF                  jmp 0x140217639
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00217761(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_00217761(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00217761&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00217761[BB_00217761]
  bb_0021776F[BB_0021776F]
```
