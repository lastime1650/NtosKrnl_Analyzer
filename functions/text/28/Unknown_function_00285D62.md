# sub_00285D62

- RVA: `0x00285D62`–`0x00285D83` (길이 `33` bytes)
- VA: `0x0000000140285D62`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00066B20`
- 디코드: `8`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00285D6B` → [MiChargeResident](MiChargeResident_function_0028A0F0.md) (function, `0x0028A0F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00285D72` → [sub_00285C73 + 0x53](Unknown_function_00285C73.md) (`tail-transfer`)
  - `0x00285D7E` → [sub_00285C73 + 0x18](Unknown_function_00285C73.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00285D62  45 33 C0                        xor r8d, r8d
00285D65  48 8B D7                        mov rdx, rdi
00285D68  49 8B CC                        mov rcx, r12
00285D6B  E8 80 43 00 00                  call 0x14028a0f0
00285D70  85 C0                           test eax, eax
00285D72  0F 84 4E FF FF FF               je 0x140285cc6
00285D78  41 BF 02 00 00 00               mov r15d, 2
00285D7E  E9 08 FF FF FF                  jmp 0x140285c8b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00285D62(__int64 a1, __int64 a2, int a3)
{
    __int64 result;

    a3 = 0;
    result = MiChargeResident(v_r12, v_rdi, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00285D62(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;

    Arg3 = 0;
    result = MiChargeResident(local_r12, local_rdi, Arg3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00285D62&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00285D62[BB_00285D62]
  bb_00285D78[BB_00285D78]
  bb_00285D62 -->|fallthrough| bb_00285D78
```
