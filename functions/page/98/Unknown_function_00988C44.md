# sub_00988C44

- RVA: `0x00988C44`–`0x00988C72` (길이 `46` bytes)
- VA: `0x0000000140988C44`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097E80`
- 디코드: `10`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00988C44` → RVA `0x00E2D7C0` (`.data`; read)
- `0x00988C58` → RVA `0x00E2D768` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00988C50` → [sub_00988B28 + 0x43](Unknown_function_00988B28.md) (`tail-transfer`)
  - `0x00988C6D` → [sub_00988B28 + 0x43](Unknown_function_00988B28.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00988C44  4C 8D 35 75 4B 4A 00            lea r14, [rip + 0x4a4b75]
00988C4B  BA 00 00 00 78                  mov edx, 0x78000000
00988C50  E9 16 FF FF FF                  jmp 0x140988b6b
00988C55  83 C0 FD                        add eax, -3
00988C58  4C 8D 35 09 4B 4A 00            lea r14, [rip + 0x4a4b09]
00988C5F  8B C8                           mov ecx, eax
00988C61  BA 00 00 00 78                  mov edx, 0x78000000
00988C66  48 C1 E1 06                     shl rcx, 6
00988C6A  4C 03 F1                        add r14, rcx
00988C6D  E9 F9 FE FF FF                  jmp 0x140988b6b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00988C44(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_00988C44(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00988C44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00988C44[BB_00988C44]
  bb_00988C55[BB_00988C55]
```
