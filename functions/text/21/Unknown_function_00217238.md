# sub_00217238

- RVA: `0x00217238`–`0x00217258` (길이 `32` bytes)
- VA: `0x0000000140217238`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005E55C`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0021724C` → [KiReleaseQueuedSpinLockInstrumented](KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00217239` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00217241` → [sub_002171C2](Unknown_function_002171C2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00217238  CC                              int3
00217239  8B 05 19 6C CF 00               mov eax, dword ptr [rip + 0xcf6c19]
0021723F  85 C0                           test eax, eax
00217241  0F 85 7B FF FF FF               jne 0x1402171c2
00217247  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
0021724C  E8 9F 07 00 00                  call 0x1402179f0
00217251  48 83 C4 20                     add rsp, 0x20
00217255  5F                              pop rdi
00217256  C3                              ret
00217257  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00217238(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;

    result = KiReleaseQueuedSpinLockInstrumented(a1, a5, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00217238(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;

    result = KiReleaseQueuedSpinLockInstrumented(Arg1, Arg5, Arg3, Arg4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00217238&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00217238[BB_00217238]
  bb_00217247[BB_00217247]
  bb_00217257[BB_00217257]
  bb_00217238 -->|fallthrough| bb_00217247
```
