# sub_006E20B8

- RVA: `0x006E20B8`–`0x006E20F8` (길이 `64` bytes)
- VA: `0x00000001406E20B8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078034`
- 디코드: `14`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E20E8` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E20DB` → [MiConvertLockedSmallPageToLarge + 0x165](../34/MiConvertLockedSmallPageToLarge_function_00347110.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E20B8  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
006E20BF  72 1F                           jb 0x1406e20e0
006E20C1  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
006E20C5  48 B9 00 00 00 00 00 02 00 00   movabs rcx, 0x20000000000
006E20CF  48 0B C1                        or rax, rcx
006E20D2  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
006E20D6  F0 48 21 77 18                  lock and qword ptr [rdi + 0x18], rsi
006E20DB  E9 95 51 C6 FF                  jmp 0x140347275
006E20E0  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
006E20E8  E8 13 9C D1 FF                  call 0x1403fbd00
006E20ED  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
006E20F1  48 85 C0                        test rax, rax
006E20F4  78 EA                           js 0x1406e20e0
006E20F6  EB C0                           jmp 0x1406e20b8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E20B8(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18)
{
    __int64 result;

    if (condition_is_below) goto loc_006E20E0;
    result = (*(unsigned __int64 *)(v_rdi + 40)) | (a1);
    *(unsigned __int64 *)(v_rdi + 40) = result;
loc_006E20E0:
    result = KeYieldProcessorEx(a18, a2, a3, a4);
    if (sign_flag) goto loc_006E20E0;
    goto loc_006E20B8;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E20B8(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, int64_t Arg18)
{
    int64_t result;

    if (condition_is_below) goto loc_006E20E0;
    result = (*(uint64_t *)(local_rdi + 0x28)) | (Arg1);
    *(uint64_t *)(local_rdi + 0x28) = result;
loc_006E20E0:
    result = KeYieldProcessorEx(Arg18, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_006E20E0;
    goto loc_006E20B8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E20B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E20B8[BB_006E20B8]
  bb_006E20C1[BB_006E20C1]
  bb_006E20E0[BB_006E20E0]
  bb_006E20F6[BB_006E20F6]
  bb_006E20B8 -->|branch| bb_006E20E0
  bb_006E20B8 -->|fallthrough| bb_006E20C1
  bb_006E20E0 -->|branch| bb_006E20E0
  bb_006E20E0 -->|fallthrough| bb_006E20F6
  bb_006E20F6 -->|branch| bb_006E20B8
```
