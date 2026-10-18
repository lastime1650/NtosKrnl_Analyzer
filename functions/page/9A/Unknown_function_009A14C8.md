# sub_009A14C8

- RVA: `0x009A14C8`–`0x009A14EE` (길이 `38` bytes)
- VA: `0x00000001409A14C8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `12`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009A14DC` → [WbMakeUserExecutablePagesKernelWritable](WbMakeUserExecutablePagesKernelWritable_function_009A14F4.md) (function, `0x009A14F4`)
- `0x009A14E7` → [WbMakeUserDataPagesKernelWritable](WbMakeUserDataPagesKernelWritable_function_009A15FC.md) (function, `0x009A15FC`)

### Direct callers
- [sub_00811EE0](../81/Unknown_function_00811EE0.md) at `0x00811F84`
- [sub_009A262C](Unknown_function_009A262C.md) at `0x009A26AE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009A14C8  48 83 EC 28                     sub rsp, 0x28
009A14CC  49 8B C1                        mov rax, r9
009A14CF  45 85 C0                        test r8d, r8d
009A14D2  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
009A14D7  4C 8B C0                        mov r8, rax
009A14DA  74 0B                           je 0x1409a14e7
009A14DC  E8 13 00 00 00                  call 0x1409a14f4
009A14E1  48 83 C4 28                     add rsp, 0x28
009A14E5  C3                              ret
009A14E6  CC                              int3
009A14E7  E8 10 01 00 00                  call 0x1409a15fc
009A14EC  EB F3                           jmp 0x1409a14e1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009A14C8(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 == 0) goto loc_009A14E7;
    result = WbMakeUserExecutablePagesKernelWritable(a1, a2, a4, a5);
loc_009A14E1:
    v_rsp = (v_rsp) + (40);
    return result;
loc_009A14E7:
    result = WbMakeUserDataPagesKernelWritable(a1, a2, a4, a5);
    goto loc_009A14E1;
}
```

## 5. (Beta) C Style

```c
int64_t sub_009A14C8(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 == 0) goto loc_009A14E7;
    result = WbMakeUserExecutablePagesKernelWritable(Arg1, Arg2, Arg4, Arg5);
loc_009A14E1:
    local_rsp = (local_rsp) + (40);
    return result;
loc_009A14E7:
    result = WbMakeUserDataPagesKernelWritable(Arg1, Arg2, Arg4, Arg5);
    goto loc_009A14E1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A14C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A14C8[BB_009A14C8]
  bb_009A14DC[BB_009A14DC]
  bb_009A14E1[BB_009A14E1]
  bb_009A14E6[BB_009A14E6]
  bb_009A14E7[BB_009A14E7]
  bb_009A14C8 -->|branch| bb_009A14E7
  bb_009A14C8 -->|fallthrough| bb_009A14DC
  bb_009A14DC -->|flow| bb_009A14E1
  bb_009A14E6 -->|flow| bb_009A14E7
  bb_009A14E7 -->|branch| bb_009A14E1
```
