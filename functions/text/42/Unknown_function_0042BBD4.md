# sub_0042BBD4

- RVA: `0x0042BBD4`–`0x0042BBEF` (길이 `27` bytes)
- VA: `0x000000014042BBD4`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A189C`
- 디코드: `6`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0042BBE5` → [HalpTimerScaleCounter](../37/HalpTimerScaleCounter_function_0037B354.md) (function, `0x0037B354`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0042BBDA` → [sub_0042B9E0 + 0xD5](Unknown_function_0042B9E0.md) (`tail-transfer`)
  - `0x0042BBEA` → [sub_0042B9E0 + 0x69](Unknown_function_0042B9E0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0042BBD4  41 BA 95 00 00 C0               mov r10d, 0xc0000095
0042BBDA  E9 D6 FE FF FF                  jmp 0x14042bab5
0042BBDF  49 8B D1                        mov rdx, r9
0042BBE2  48 8B CB                        mov rcx, rbx
0042BBE5  E8 6A F7 F4 FF                  call 0x14037b354
0042BBEA  E9 5A FE FF FF                  jmp 0x14042ba49
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0042BBD4(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
}
```

## 5. (Beta) C Style

```c
int64_t sub_0042BBD4(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042BBD4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0042BBD4[BB_0042BBD4]
  bb_0042BBDF[BB_0042BBDF]
```
