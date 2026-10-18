# sub_0089A36F

- RVA: `0x0089A36F`–`0x0089A39B` (길이 `44` bytes)
- VA: `0x000000014089A36F`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007E5E4`
- 디코드: `11`개 명령, `44/44` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0089A374` → [sub_0089A0DA + 0x245](Unknown_function_0089A0DA.md) (`tail-transfer`)
  - `0x0089A383` → [sub_0089A0DA + 0x201](Unknown_function_0089A0DA.md) (`tail-transfer`)
  - `0x0089A38F` → [sub_0089A0DA + 0x201](Unknown_function_0089A0DA.md) (`tail-transfer`)
  - `0x0089A399` → [sub_0089A0DA + 0x245](Unknown_function_0089A0DA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0089A36F  B8 9A 00 00 C0                  mov eax, 0xc000009a
0089A374  EB A9                           jmp 0x14089a31f
0089A376  80 CA 02                        or dl, 2
0089A379  88 50 1B                        mov byte ptr [rax + 0x1b], dl
0089A37C  41 F7 07 00 00 01 00            test dword ptr [r15], 0x10000
0089A383  0F 84 52 FF FF FF               je 0x14089a2db
0089A389  80 CA 04                        or dl, 4
0089A38C  88 50 1B                        mov byte ptr [rax + 0x1b], dl
0089A38F  E9 47 FF FF FF                  jmp 0x14089a2db
0089A394  B8 0D 00 00 C0                  mov eax, 0xc000000d
0089A399  EB 84                           jmp 0x14089a31f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0089A36F(__int64 a1, unsigned __int8 a2)
{
}
```

## 5. (Beta) C Style

```c
int64_t sub_0089A36F(int64_t Arg1, uint8_t Arg2)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0089A36F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0089A36F[BB_0089A36F]
  bb_0089A376[BB_0089A376]
  bb_0089A389[BB_0089A389]
  bb_0089A394[BB_0089A394]
  bb_0089A376 -->|fallthrough| bb_0089A389
```
