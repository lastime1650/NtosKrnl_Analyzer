# FsRtlpRequestShareableOplock$fin$0

- RVA: `0x006D52F1`–`0x006D531A` (길이 `41` bytes)
- VA: `0x00000001406D52F1`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000C6020`
- 디코드: `14`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D530D` → [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D52F1  40 55                           push rbp
006D52F3  48 83 EC 40                     sub rsp, 0x40
006D52F7  48 8B EA                        mov rbp, rdx
006D52FA  80 7D 44 00                     cmp byte ptr [rbp + 0x44], 0
006D52FE  74 13                           je 0x1406d5313
006D5300  81 7D 70 00 00 01 00            cmp dword ptr [rbp + 0x70], 0x10000
006D5307  74 0A                           je 0x1406d5313
006D5309  48 8B 4D 78                     mov rcx, qword ptr [rbp + 0x78]
006D530D  E8 8E B0 B7 FF                  call 0x1402503a0
006D5312  90                              nop
006D5313  48 83 C4 40                     add rsp, 0x40
006D5317  5D                              pop rbp
006D5318  C3                              ret
006D5319  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlpRequestShareableOplock_fin_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (64);
    if ((*(unsigned __int8 *)(a2 + 68)) == 0) goto loc_006D5313;
    if ((*(unsigned int *)(a2 + 112)) != 0x10000ULL) {
        a1 = *(unsigned __int64 *)(a2 + 120);
        result = ExReleaseFastMutexUnsafe(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlpRequestShareableOplock_fin_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (64);
    if ((*(uint8_t *)(arg2 + 0x44)) == 0) goto loc_006D5313;
    if ((*(uint32_t *)(arg2 + 0x70)) != 0x10000ULL) {
        Arg1 = *(uint64_t *)(arg2 + 0x78);
        result = ExReleaseFastMutexUnsafe(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x44` | `8` | `R` |
| `Arg2` | `+ 0x70` | `32` | `R` |
| `Arg2` | `+ 0x78` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D52F1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D52F1[BB_006D52F1]
  bb_006D5300[BB_006D5300]
  bb_006D5309[BB_006D5309]
  bb_006D5313[BB_006D5313]
  bb_006D5319[BB_006D5319]
  bb_006D52F1 -->|branch| bb_006D5313
  bb_006D52F1 -->|fallthrough| bb_006D5300
  bb_006D5300 -->|branch| bb_006D5313
  bb_006D5300 -->|fallthrough| bb_006D5309
  bb_006D5309 -->|flow| bb_006D5313
```
