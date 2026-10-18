# FsRtlCurrentBatchOplock

- RVA: `0x009FDC50`–`0x009FDC72` (길이 `34` bytes)
- VA: `0x00000001409FDC50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `34/34` bytes 표시
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
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009FDC50  48 8B 01                        mov rax, qword ptr [rcx]
009FDC53  33 D2                           xor edx, edx
009FDC55  48 85 C0                        test rax, rax
009FDC58  75 04                           jne 0x1409fdc5e
009FDC5A  8A C2                           mov al, dl
009FDC5C  C3                              ret
009FDC5D  CC                              int3
009FDC5E  F6 80 90 00 00 00 0C            test byte ptr [rax + 0x90], 0xc
009FDC65  B9 01 00 00 00                  mov ecx, 1
009FDC6A  0F B6 D2                        movzx edx, dl
009FDC6D  0F 45 D1                        cmovne edx, ecx
009FDC70  EB E8                           jmp 0x1409fdc5a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlCurrentBatchOplock(__int64 a1, int a2)
{
    a2 = 0;
    if (*(unsigned __int64 *)(a1) != 0) goto loc_009FDC5E;
loc_009FDC5A:
    return 0;
loc_009FDC5E:
    a2 = 0;
    if (((*(unsigned __int8 *)(0 + 144)) & (12)) != 0) { a2 = 1; }
    goto loc_009FDC5A;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlCurrentBatchOplock(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    Arg2 = 0;
    if (*(uint64_t *)(arg1) != 0) goto loc_009FDC5E;
loc_009FDC5A:
    return 0;
loc_009FDC5E:
    Arg2 = 0;
    if (((*(uint8_t *)(0 + 0x90)) & (12)) != 0) { Arg2 = 1; }
    goto loc_009FDC5A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009FDC50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009FDC50[BB_009FDC50]
  bb_009FDC5A[BB_009FDC5A]
  bb_009FDC5D[BB_009FDC5D]
  bb_009FDC5E[BB_009FDC5E]
  bb_009FDC50 -->|branch| bb_009FDC5E
  bb_009FDC50 -->|fallthrough| bb_009FDC5A
  bb_009FDC5D -->|flow| bb_009FDC5E
  bb_009FDC5E -->|branch| bb_009FDC5A
```
