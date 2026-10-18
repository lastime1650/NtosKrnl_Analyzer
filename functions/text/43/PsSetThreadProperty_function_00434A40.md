# PsSetThreadProperty

- RVA: `0x00434A40`–`0x00434A6B` (길이 `43` bytes)
- VA: `0x0000000140434A40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00434A4A` → [PspValidateThread](PspValidateThread_function_00434A80.md) (function, `0x00434A80`)
- `0x00434A60` → [PspSetPropertyHelper](PspSetPropertyHelper_function_00434B08.md) (function, `0x00434B08`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00434A40  48 83 EC 28                     sub rsp, 0x28
00434A44  4D 8B C8                        mov r9, r8
00434A47  4C 8B D2                        mov r10, rdx
00434A4A  E8 31 00 00 00                  call 0x140434a80
00434A4F  85 C0                           test eax, eax
00434A51  78 12                           js 0x140434a65
00434A53  48 81 C1 58 06 00 00            add rcx, 0x658
00434A5A  4D 8B C1                        mov r8, r9
00434A5D  49 8B D2                        mov rdx, r10
00434A60  E8 A3 00 00 00                  call 0x140434b08
00434A65  48 83 C4 28                     add rsp, 0x28
00434A69  C3                              ret
00434A6A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsSetThreadProperty(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PspValidateThread(a1, a2, a3, a3);
    if (!(sign_flag)) {
        a1 = (a1) + (0x658ULL);
        a3 = a3;
        a2 = a2;
        result = PspSetPropertyHelper(a1, a2, a3, a3);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsSetThreadProperty(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PspValidateThread(Arg1, Arg2, Arg3, Arg3);
    if (!(sign_flag)) {
        Arg1 = (Arg1) + (0x658ULL);
        Arg3 = Arg3;
        Arg2 = Arg2;
        result = PspSetPropertyHelper(Arg1, Arg2, Arg3, Arg3);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00434A40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00434A40[BB_00434A40]
  bb_00434A53[BB_00434A53]
  bb_00434A65[BB_00434A65]
  bb_00434A6A[BB_00434A6A]
  bb_00434A40 -->|branch| bb_00434A65
  bb_00434A40 -->|fallthrough| bb_00434A53
  bb_00434A53 -->|flow| bb_00434A65
```
