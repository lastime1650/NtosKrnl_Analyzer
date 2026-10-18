# sub_006E2024

- RVA: `0x006E2024`–`0x006E206A` (길이 `70` bytes)
- VA: `0x00000001406E2024`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000774B8`
- 디코드: `16`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E2030` → [CcAcquireBcbLockAndVacbLock](../26/CcAcquireBcbLockAndVacbLock_function_0026FC58.md) (function, `0x0026FC58`)
- `0x006E2047` → [SetVacb](../27/SetVacb_function_00273340.md) (function, `0x00273340`)
- `0x006E2052` → [CcReleaseBcbLockAndVacbLock](../2D/CcReleaseBcbLockAndVacbLock_function_002DFDF0.md) (function, `0x002DFDF0`)
- `0x006E205F` → [CcFreeUnusedVacbLevels](../27/CcFreeUnusedVacbLevels_function_00273B1C.md) (function, `0x00273B1C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E2065` → [CcPinFileData + 0xBA](../33/CcPinFileData_function_0033FB40.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E2024  48 8B D6                        mov rdx, rsi
006E2027  41 BF 01 00 00 00               mov r15d, 1
006E202D  41 8B CF                        mov ecx, r15d
006E2030  E8 23 DC B8 FF                  call 0x14026fc58
006E2035  4C 8D 8C 24 C0 00 00 00         lea r9, [rsp + 0xc0]
006E203D  4D 8D 47 FE                     lea r8, [r15 - 2]
006E2041  48 8B D3                        mov rdx, rbx
006E2044  48 8B CE                        mov rcx, rsi
006E2047  E8 F4 12 B9 FF                  call 0x140273340
006E204C  48 8B D6                        mov rdx, rsi
006E204F  41 8B CF                        mov ecx, r15d
006E2052  E8 99 DD BF FF                  call 0x1402dfdf0
006E2057  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
006E205F  E8 B8 1A B9 FF                  call 0x140273b1c
006E2064  90                              nop
006E2065  E9 90 DB C5 FF                  jmp 0x14033fbfa
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E2024(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24)
{
    __int64 result;

    result = CcAcquireBcbLockAndVacbLock(1, v_rsi, a3, a4);
    result = SetVacb(v_rsi, v_rbx, 1 - 2, a24);
    result = CcReleaseBcbLockAndVacbLock(1, v_rsi, 1 - 2, a24);
    result = CcFreeUnusedVacbLevels(a24, v_rsi, 1 - 2, a24);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E2024(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, int64_t Arg24)
{
    int64_t result;

    result = CcAcquireBcbLockAndVacbLock(1, local_rsi, Arg3, Arg4);
    result = SetVacb(local_rsi, local_rbx, 1 - 2, Arg24);
    result = CcReleaseBcbLockAndVacbLock(1, local_rsi, 1 - 2, Arg24);
    result = CcFreeUnusedVacbLevels(Arg24, local_rsi, 1 - 2, Arg24);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E2024&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E2024[BB_006E2024]
```
