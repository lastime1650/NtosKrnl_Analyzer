# EtwpCreateEventKey

- RVA: `0x0043C6B0`–`0x0043C6EB` (길이 `59` bytes)
- VA: `0x000000014043C6B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) at `0x00AF405C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043C6B0  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0043C6B9  41 B8 01 00 00 00               mov r8d, 1
0043C6BF  48 8B 82 A8 8B 00 00            mov rax, qword ptr [rdx + 0x8ba8]
0043C6C6  F0 4C 0F C1 40 08               lock xadd qword ptr [rax + 8], r8
0043C6CC  8B 42 24                        mov eax, dword ptr [rdx + 0x24]
0043C6CF  49 FF C0                        inc r8
0043C6D2  48 BA FF FF FF FF FF FF 00 00   movabs rdx, 0xffffffffffff
0043C6DC  48 C1 E0 30                     shl rax, 0x30
0043C6E0  4C 23 C2                        and r8, rdx
0043C6E3  49 0B C0                        or rax, r8
0043C6E6  48 89 01                        mov qword ptr [rcx], rax
0043C6E9  C3                              ret
0043C6EA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCreateEventKey(__int64 a1)
{
    __int64 result;

    a3 = (1) + 1;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36))) << (48);
    a3 = (a3) & (*(unsigned __int64 *)(gs_base + (0 + 32)));
    result = (result) | (a3);
    *(unsigned __int64 *)(a1) = result;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCreateEventKey(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    a3 = (1) + 1;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24))) << (48);
    a3 = (a3) & (*(uint64_t *)(gs_base + (0 + 0x20)));
    result = (result) | (a3);
    *(uint64_t *)(arg1) = result;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043C6B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043C6B0[BB_0043C6B0]
  bb_0043C6EA[BB_0043C6EA]
```
