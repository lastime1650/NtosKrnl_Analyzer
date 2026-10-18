# sub_00205F94

- RVA: `0x00205F94`–`0x00205FB8` (길이 `36` bytes)
- VA: `0x0000000140205F94`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CE20`
- 디코드: `8`개 명령, `36/36` bytes 표시
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
  - `0x00205F9A` → [sub_00206312 + 0x2D](Unknown_function_00206312.md) (`tail-transfer`)
  - `0x00205FA3` → [sub_00206190](Unknown_function_00206190.md) (`tail-transfer`)
  - `0x00205FB6` → [sub_00205FB8 + 0x16](Unknown_function_00205FB8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00205F94  81 FB 06 00 00 C0               cmp ebx, 0xc0000006
00205F9A  0F 84 9F 03 00 00               je 0x14020633f
00205FA0  4D 85 ED                        test r13, r13
00205FA3  0F 85 E7 01 00 00               jne 0x140206190
00205FA9  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00205FAE  45 85 E4                        test r12d, r12d
00205FB1  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00205FB6  74 16                           je 0x140205fce
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00205F94(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14)
{
}
```

## 5. (Beta) C Style

```c
void sub_00205F94(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, int64_t Arg13, int64_t Arg14)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00205F94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00205F94[BB_00205F94]
  bb_00205FA0[BB_00205FA0]
  bb_00205FA9[BB_00205FA9]
  bb_00205F94 -->|fallthrough| bb_00205FA0
  bb_00205FA0 -->|fallthrough| bb_00205FA9
```
