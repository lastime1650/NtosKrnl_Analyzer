# KiPlatformSwapStacksAndCall

- RVA: `0x006B96C0`–`0x006B96D4` (길이 `20` bytes)
- VA: `0x00000001406B96C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C22F8`
- 디코드: `9`개 명령, `20/20` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006B96CC` → [KxPlatformSwapStacksAndCall](KxPlatformSwapStacksAndCall_function_006B96E0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006B96C0  48 55                           push rbp
006B96C2  48 8B EC                        mov rbp, rsp
006B96C5  49 89 60 40                     mov qword ptr [r8 + 0x40], rsp
006B96C9  49 8B E0                        mov rsp, r8
006B96CC  EB 12                           jmp 0x1406b96e0
006B96CE  CC                              int3
006B96CF  48 8B E5                        mov rsp, rbp
006B96D2  5D                              pop rbp
006B96D3  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KiPlatformSwapStacksAndCall(__int64 a1, __int64 a2, __int64 a3)
{
    *(unsigned __int64 *)(a3 + 64) = v_rsp;
}
```

## 5. (Beta) C Style

```c
void KiPlatformSwapStacksAndCall(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    *(uint64_t *)(arg3 + 0x40) = local_rsp;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x40` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B96C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006B96C0[BB_006B96C0]
  bb_006B96CE[BB_006B96CE]
```
