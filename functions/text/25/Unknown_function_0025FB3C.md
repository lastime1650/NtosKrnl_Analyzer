# sub_0025FB3C

- RVA: `0x0025FB3C`–`0x0025FB5C` (길이 `32` bytes)
- VA: `0x000000014025FB3C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006433C`
- 디코드: `7`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0025FB52` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0025FB3C` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0025FB44` → [sub_0025FA63 + 0x4E](Unknown_function_0025FA63.md) (`tail-transfer`)
  - `0x0025FB57` → [sub_0025FA63 + 0x5F](Unknown_function_0025FA63.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0025FB3C  8B 05 16 E3 CA 00               mov eax, dword ptr [rip + 0xcae316]
0025FB42  85 C0                           test eax, eax
0025FB44  0F 85 67 FF FF FF               jne 0x14025fab1
0025FB4A  48 8B D7                        mov rdx, rdi
0025FB4D  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025FB52  E8 F9 5C 01 00                  call 0x140275850
0025FB57  E9 66 FF FF FF                  jmp 0x14025fac2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0025FB3C(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;

    result = KiAcquireQueuedSpinLockInstrumented(a9, v_rdi, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0025FB3C(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, int64_t Arg9)
{
    int64_t result;

    result = KiAcquireQueuedSpinLockInstrumented(Arg9, local_rdi, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0025FB3C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0025FB3C[BB_0025FB3C]
  bb_0025FB4A[BB_0025FB4A]
  bb_0025FB3C -->|fallthrough| bb_0025FB4A
```
