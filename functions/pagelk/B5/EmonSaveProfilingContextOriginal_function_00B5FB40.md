# EmonSaveProfilingContextOriginal

- RVA: `0x00B5FB40`–`0x00B5FB6A` (길이 `42` bytes)
- VA: `0x0000000140B5FB40`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `13`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B5FB52` → [EmonSaveProfilingContextInternalOriginal](../../text/55/EmonSaveProfilingContextInternalOriginal_function_0055FCE4.md) (function, `0x0055FCE4`)
- `0x00B5FB5E` → [EmonSaveProfilingContextInternalOriginal](../../text/55/EmonSaveProfilingContextInternalOriginal_function_0055FCE4.md) (function, `0x0055FCE4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B5FB52` → [EmonSaveProfilingContextInternalOriginal](../../text/55/EmonSaveProfilingContextInternalOriginal_function_0055FCE4.md) (`PAGELK` → `.text`)
  - `0x00B5FB5E` → [EmonSaveProfilingContextInternalOriginal](../../text/55/EmonSaveProfilingContextInternalOriginal_function_0055FCE4.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B5FB40  40 53                           push rbx
00B5FB42  48 83 EC 20                     sub rsp, 0x20
00B5FB46  65 8B 1C 25 A4 01 00 00         mov ebx, dword ptr gs:[0x1a4]
00B5FB4E  33 C9                           xor ecx, ecx
00B5FB50  8B D3                           mov edx, ebx
00B5FB52  E8 8D 01 A0 FF                  call 0x14055fce4
00B5FB57  8B D3                           mov edx, ebx
00B5FB59  B9 01 00 00 00                  mov ecx, 1
00B5FB5E  E8 81 01 A0 FF                  call 0x14055fce4
00B5FB63  48 83 C4 20                     add rsp, 0x20
00B5FB67  5B                              pop rbx
00B5FB68  C3                              ret
00B5FB69  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmonSaveProfilingContextOriginal(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = 0;
    result = EmonSaveProfilingContextInternalOriginal(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))), a3, a4);
    result = EmonSaveProfilingContextInternalOriginal(1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EmonSaveProfilingContextOriginal(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    result = EmonSaveProfilingContextInternalOriginal(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))), a3, a4);
    result = EmonSaveProfilingContextInternalOriginal(1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B5FB40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B5FB40[BB_00B5FB40]
  bb_00B5FB69[BB_00B5FB69]
```
