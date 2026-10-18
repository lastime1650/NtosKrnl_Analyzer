# sub_00207C21

- RVA: `0x00207C21`–`0x00207C3E` (길이 `29` bytes)
- VA: `0x0000000140207C21`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2E4`
- 디코드: `7`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00207C37` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00207C21` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00207C29` → [sub_00207BC1 + 0x1C](Unknown_function_00207BC1.md) (`tail-transfer`)
  - `0x00207C3C` → [sub_00207BC1 + 0x25](Unknown_function_00207BC1.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00207C21  8B 05 31 62 D0 00               mov eax, dword ptr [rip + 0xd06231]
00207C27  85 C0                           test eax, eax
00207C29  75 B2                           jne 0x140207bdd
00207C2B  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
00207C30  48 8D 8B 18 06 00 00            lea rcx, [rbx + 0x618]
00207C37  E8 B4 B2 18 00                  call 0x140392ef0
00207C3C  EB A8                           jmp 0x140207be6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00207C21(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;

    result = KiReleaseSpinLockInstrumented(v_rbx + 1560, a5, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00207C21(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;

    result = KiReleaseSpinLockInstrumented(local_rbx + 1560, Arg5, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00207C21&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00207C21[BB_00207C21]
  bb_00207C2B[BB_00207C2B]
  bb_00207C21 -->|fallthrough| bb_00207C2B
```
